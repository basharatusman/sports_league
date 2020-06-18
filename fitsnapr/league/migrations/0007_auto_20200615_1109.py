# Generated by Django 3.0.3 on 2020-06-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_auto_20200615_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='team',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='team',
            name='max_players',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='team',
            name='min_players',
            field=models.IntegerField(default=5),
        ),
    ]