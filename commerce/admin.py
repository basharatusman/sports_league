from django.contrib import admin
from . models import LeaguePackage, LeagueCart, LeagueOrder, Category


admin.site.register(Category)
admin.site.register(LeaguePackage)
admin.site.register(LeagueCart)
admin.site.register(LeagueOrder)
