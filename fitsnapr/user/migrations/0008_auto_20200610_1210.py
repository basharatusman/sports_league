# Generated by Django 3.0.3 on 2020-06-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200609_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
