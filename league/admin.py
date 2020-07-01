from django.contrib import admin
from .models import Sport, Season, Schedule, Team, Game, GameLocation, TeamPlayer

admin.site.register(Sport)
admin.site.register(Season)
admin.site.register(Schedule)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(GameLocation)
admin.site.register(TeamPlayer)
