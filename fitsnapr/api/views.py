from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from user.models import UserProfile
from league.models import Schedule, Team, TeamPlayer

stripe.api_key = settings.STRIPE_API_KEY
endpoint_secret = settings.STRIPE_ENDPOINT_KEY


def api(request):
    return render(request, 'api/api.html')


def create_payment(request):
    data = json.loads(request.body)
    print(request.user)
    if request.method == 'POST':
        try:
            intent = stripe.PaymentIntent.create(amount=500, currency='cad')
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse(status=404, data={'status': 'false', 'message': str(e)})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print('payment was successful')

    elif event.type == 'payment_method.attached':
        payment_method = event.data.object
        print('payment method was attached to a customer')

    elif event.type == 'payment_intent.created':
        payment_intent = event.data.object
        print('payment intent created')

    else:
        return HttpResponse(status=400)

    return HttpResponse(status=200)


def add_player_to_team(request, *args, **kwargs):
    # get the user profile
    # get the schedule they purchased
    # look up public teams for that schedule
    # if public_team exists & < max players, add player
    # otherwise create public team and add player while max schedule teams < # of teams

    user = UserProfile.objects.get(id=request.user.userprofile.id)
    schedule = Schedule.objects.get(id=1)  # pass in as kwarg
    teams = Team.objects.filter(schedule=schedule, is_public=True)

    if teams.count() >= 1 and teams.count() <= schedule.team_limit:
        for team in teams:
            if team.player.all().count() < team.max_players:
                TeamPlayer(team=team, player=user).save()
                return HttpResponse('success')

        if teams.count() < team.max_players:
            team = Team.objects.create(
                schedule=schedule, team_name=f'Team {teams.count() + 1}', max_players=3, min_players=1)
            TeamPlayer(team=team, player=user).save()

    elif teams.count() == 0:
        team = Team.objects.create(
            schedule=schedule, team_name=f'Team {teams.count() + 1}', max_players=3, min_players=1)
        TeamPlayer(team=team, player=user).save()

    else:
        # add player to unsorted
        pass

    return HttpResponse('Hello')


def add_team_to_schedule(request, *args, **kwargs):
    # get schedule
    # add team
    # get player
    # set team is_public to False

    user = UserProfile.objects.get(id=request.user.userprofile.id)
    schedule = Schedule.objects.get(id=1)  # pass in schedule id as kwarg
    max_player = 10  # pass in as kwarg
    min_player = 4  # pass in as kwarg
    team_name = 'Team 1'  # pass in as kwarg
    team = Team.objects.create(schedule=schedule, team_name=team_name,
                               max_players=max_player, min_players=min_player, is_public=False)

    TeamPlayer(team=team, player=user).save()

    return HttpResponse('success')
