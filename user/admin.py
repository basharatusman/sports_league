from django.contrib import admin
from . models import UserProfile, ShippingAddress, BillingAddress

admin.site.register(UserProfile)
admin.site.register(ShippingAddress)
admin.site.register(BillingAddress)
