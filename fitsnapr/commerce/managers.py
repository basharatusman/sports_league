from django.db import models
from django.apps import apps


class CartQuerySet(models.QuerySet):

    def get_cart_items(self, request):
        LeagueCart = apps.get_model(app_label='commerce', model_name='LeagueCart')

        return LeagueCart.objects.filter(
            user_profile=request.user.userprofile, leagueorder__ordered=False)

    def get_cart_total(self, request, cart_items):
        cart_total = 0
        for item in cart_items:
            cart_total += item.league_package.price * item.quantity

        return cart_total


class LeagueCartManager(models.Manager):

    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)

    def get_cart_items(self, request):
        return self.get_queryset().get_cart_items(request)

    def get_cart_total(self, request, cart_items):
        return self.get_queryset().get_cart_total(request, cart_items)
