from django.contrib import admin
from . models import Package, OrderItem, Order


admin.site.register(Package)
admin.site.register(OrderItem)
admin.site.register(Order)
