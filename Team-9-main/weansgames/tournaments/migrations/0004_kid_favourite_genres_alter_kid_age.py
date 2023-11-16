# Generated by Django 4.2.6 on 2023-10-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_event_max_no_of_players_event_online_event_players_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='favourite_genres',
            field=models.ManyToManyField(to='tournaments.genre'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
