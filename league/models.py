from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint, Q
from user.models import UserProfile
from django.core.exceptions import ValidationError


class Sport(models.Model):
    sport_name = models.CharField(max_length=50, blank=False)
    is_team_sport = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sport_name

    class Meta:
        verbose_name_plural = 'Sports'


class Season(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    season_start_date = models.DateField()
    season_end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sport.sport_name} season ending {self.season_end_date}"

    class Meta:
        verbose_name_plural = 'Seasons'


class Schedule(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    day_choices = [('M', "Monday"), ('T', "Tuesday"), ('W', "Wednesday"), ('T', "Thursday"),
                   ('F', "Friday"), ('S', "Saturday"), ('U', "Sunday")]
    schedule_day = models.CharField(
        max_length=30, choices=day_choices, default=1)
    type_choices = [('Co-ed', 'Co-ed'), ("Men's", "Men's"),
                    ("Women's", "Women's")]
    schedule_type = models.CharField(
        max_length=30, choices=type_choices, default=1)
    compete_choices = [('Beg', "Beginner"), ('Int', 'Intermediate'),
                       ('Adv', 'Advanced')]
    compete_type = models.CharField(
        max_length=30, choices=compete_choices, default=1)
    team_limit = models.IntegerField(default=10)
    schedule_description = models.TextField(blank=True)

    @property
    def schedule_name(self):
        return (f'{self.schedule_day} {self.schedule_type} {self.compete_type}')

    def __str__(self):
        return self.schedule_name

    class Meta:
        verbose_name_plural = 'Schedules'


class Team(models.Model):
    schedule = models.ForeignKey(
        Schedule, on_delete=models.SET_NULL, null=True)
    player = models.ManyToManyField(UserProfile, through='TeamPlayer')
    team_name = models.CharField(max_length=50, default='')
    max_players = models.IntegerField(default=10)
    min_players = models.IntegerField(default=5)
    is_public = models.BooleanField(default=True)

    @property
    def team_status(self):
        # return if team is current, past or future
        pass

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name_plural = 'Teams'


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.player.user.username} on {self.team}'

    class Meta:
        unique_together = ['team', 'player']


class GameLocation(models.Model):
    location_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = 'Game Location'


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

    def save(self, *args, **kwargs):
        if self.home_team == self.away_team:
            raise ValidationError(message='teams must be unique')

        else:
            super(Game, self).save(*args, **kwargs)

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

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.game_date} at {self.game_time}"

    class Meta:
        verbose_name_plural = 'Game'
