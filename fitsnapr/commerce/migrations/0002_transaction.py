# Generated by Django 3.0.3 on 2020-06-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_stripe_customer'),
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(blank=True, max_length=50)),
                ('amount_charged', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('last_digits', models.CharField(blank=True, max_length=4)),
                ('network', models.CharField(blank=True, max_length=20)),
                ('payment_intent', models.CharField(blank=True, max_length=50)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commerce.LeagueOrder')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
