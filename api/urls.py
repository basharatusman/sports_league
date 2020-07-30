from django.urls import path, include
from .views import api, create_payment, stripe_webhook, add_player_to_team, add_team_to_schedule
from .serializer_views import UserList, UserDetail, UserProfileView


urlpatterns = [
    path('', api, name='api-view'),
    path('create-payment-intent/', create_payment, name='create-payment-intent'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('add/', add_team_to_schedule, name='add'),
    path('user/', UserList.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
