from django.urls import path
from .views import api, create_payment, stripe_webhook, add_to_team


urlpatterns = [
    path('', api, name='api-view'),
    path('create-payment-intent/', create_payment, name='create-payment-intent'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('add/', add_to_team, name='add'),
]
