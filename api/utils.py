from commerce.models import Transaction
from commerce.models import LeagueOrder
from user.models import UserProfile


def create_transaction(payment_intent):
    user_profile = UserProfile.objects.get(id=1)
    order = LeagueOrder.objects.get(id=1)  # order object
    stripe_charge_id = payment_intent.get('charges').get('data')[0].get('id')
    amount_charged = payment_intent.get('charges').get('data')[0].get('amount')
    last_digits = payment_intent.get('charges').get('data')[0].get(
        'payment_method_details').get('card').get('last4')
    network = payment_intent.get('charges').get('data')[0].get(
        'payment_method_details').get('card').get('network')
    payment_intent = payment_intent.get('id')

    Transaction.objects.create(user_profile=user_profile, order=order, stripe_charge_id=stripe_charge_id,
                               amount_charged=amount_charged, last_digits=last_digits, network=network, payment_intent=payment_intent)
