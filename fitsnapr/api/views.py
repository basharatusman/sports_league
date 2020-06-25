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


def add_to_team(request):
    user = UserProfile.objects.get(id=request.user.userprofile.id)
    schedule = Schedule.objects.get(id=1)
    teams = Team.objects.filter(schedule=schedule, is_public=True)

    if teams.count() < schedule.team_limit:
        for team in teams:
            if team.player.all().count() < team.max_players:
                TeamPlayer(team=team, player=user).save()
                break

    return HttpResponse('Hello')

    # get the user profile
    # get the schedule they purchased
    # look up public teams for that schedule
    # if public_team exists & < max players, add player
    # otherwise create public team and add player while max schedule teams < # of teams
