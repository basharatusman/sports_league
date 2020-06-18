from django.db import models
from league.models import Schedule
from user.models import UserProfile


class Package(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    package_choices = [('Individual', 'Individual'), ('Team', 'Team')]
    package_type = models.CharField(max_length=30, choices=package_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def package_name(self):
        return (f"{self.package_type} {self.schedule.schedule_name}")

    def __str__(self):
        return (f"{self.package_type} {self.schedule.schedule_name}")

    class Meta:
        verbose_name_plural = 'Packages'


class OrderItem(models.Model):
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package.package_name

    class Meta:
        verbose_name_plural = 'Order Items'


class Order(models.Model):
    customer = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField()
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Order'
