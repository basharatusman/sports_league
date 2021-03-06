# Generated by Django 3.0.3 on 2020-06-26 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Game Location',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_day', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('T', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday'), ('U', 'Sunday')], default=1, max_length=30)),
                ('schedule_type', models.CharField(choices=[('Co-ed', 'Co-ed'), ("Men's", "Men's"), ("Women's", "Women's")], default=1, max_length=30)),
                ('compete_type', models.CharField(choices=[('Beg', 'Beginner'), ('Int', 'Intermediate'), ('Adv', 'Advanced')], default=1, max_length=30)),
                ('team_limit', models.IntegerField(default=10)),
                ('schedule_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=50)),
                ('is_team_sport', models.BooleanField(default=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Sports',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='', max_length=50)),
                ('max_players', models.IntegerField(default=10)),
                ('min_players', models.IntegerField(default=5)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserProfile')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='player',
            field=models.ManyToManyField(through='league.TeamPlayer', to='user.UserProfile'),
        ),
        migrations.AddField(
            model_name='team',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.Schedule'),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_start_date', models.DateField()),
                ('season_end_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.Sport')),
            ],
            options={
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.Season'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField()),
                ('game_time', models.TimeField()),
                ('home_team_score', models.IntegerField(default=0)),
                ('away_team_score', models.IntegerField(default=0)),
                ('away_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_team', to='league.Team')),
                ('game_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.GameLocation')),
                ('home_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_team', to='league.Team')),
            ],
        ),
    ]
