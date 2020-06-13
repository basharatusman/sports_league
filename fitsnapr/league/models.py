from django.db import models
from user.models import UserProfile


class Sport(models.Model):
    sport_name = models.CharField(max_length=50, blank=False)
    is_team_sport = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.sport_name


class Season(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    season_start_date = models.DateField()
    season_end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Seasons'

    def __str__(self):
        return f"{self.sport.sport_name} season ending {self.season_end_date}"


class Schedule(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    schedule_name = models.CharField(max_length=30)
    team_limit = models.IntegerField(default=10)
    schedule_description = models.TextField()

    class Meta:
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return self.schedule_name


class Team(models.Model):
    schedule = models.ForeignKey(
        Schedule, on_delete=models.SET_NULL, null=True)
    player = models.ManyToManyField(UserProfile)
    team_name = models.CharField(max_length=50, default='')

    class Meta:
        pass

    @property
    def team_status(self):
        # return if team is current, past or future
        pass

    def __str__(self):
        return self.team_name


class GameLocation(models.Model):
    location_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'GameLocations'

    def __str__(self):
        return self.location_name


class Game(models.Model):
    home_team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='home_team')
    away_team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='away_team')
    game_location = models.ForeignKey(
        GameLocation, on_delete=models.SET_NULL, null=True)
    game_date = models.DateField()
    game_time = models.TimeField()
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)

    @property
    def winning_team(self):
        if self.home_team_score != self.away_team_score:
            return self.home_team if (self.home_team_score > self.away_team_score) else self.away_team
        else:
            return "ND"

    @property
    def losing_team(self):
        if self.home_team_score != self.away_team_score:
            return self.home_team if (self.home_team_score < self.away_team_score) else self.away_team
        else:
            return "ND"

    @property
    def is_tied(self):
        return self.home_team_score == self.away_team_score

        class Meta:
            pass

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.game_date} at {self.game_time}"
