from django.db import models
from league.models import Schedule
from user.models import UserProfile
from . managers import LeagueCartManager


class Category(models.Model):
    category_choices = [('League', 'Sports League'), ('Fitness', 'Online Fitness')]
    category_name = models.CharField(max_length=30, choices=category_choices)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Catagories'


class LeaguePackage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    package_choices = [('Ind', 'Individual'), ('Team', 'Team')]
    package_type = models.CharField(max_length=15, choices=package_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def package_name(self):
        return (f"{self.package_type} {self.schedule.schedule_name}")

    def __str__(self):
        return (f"{self.package_name}")

    class Meta:
        verbose_name_plural = 'Packages'


class LeagueCart(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    league_package = models.ForeignKey(LeaguePackage, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    cart_manager = LeagueCartManager()

    @property
    def cart_item_total(self):
        return self.league_package.price * self.quantity

    def __str__(self):
        return self.league_package.package_name

    class Meta:
        verbose_name_plural = 'Cart'


class LeagueOrder(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    league_packages = models.ManyToManyField(LeagueCart, through='LeagueOrderPackage')
    ordered = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user}'s order created {self.date_created}'"

    class Meta:
        verbose_name_plural = 'Orders'


class LeagueOrderPackage(models.Model):
    league_order = models.ForeignKey(LeagueOrder, on_delete=models.CASCADE)
    league_packages = models.ForeignKey(LeagueCart, on_delete=models.CASCADE)


class Transaction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(LeagueOrder, on_delete=models.SET_NULL, null=True)
    stripe_charge_id = models.CharField(max_length=50, blank=True)
    amount_charged = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    last_digits = models.CharField(max_length=4, blank=True)
    network = models.CharField(max_length=20, blank=True)
    payment_intent = models.CharField(max_length=50, blank=True)
