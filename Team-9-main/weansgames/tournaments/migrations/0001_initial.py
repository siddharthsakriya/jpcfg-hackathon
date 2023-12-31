
# Generated by Django 4.1 on 2023-10-08 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_choice', models.CharField(choices=[('N', 'Nurse'), ('D', 'Doctor'), ('A', 'Admin')], default='N', max_length=2)),
                ('surname', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=15)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tournaments.player')),
                ('age', models.IntegerField()),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isVerified', models.BooleanField()),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tournaments.player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_one_won', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.event')),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player_two_set', to='tournaments.player')),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player_one_set', to='tournaments.player')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=1024)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.genre')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.game'),
        ),
        migrations.CreateModel(
            name='PlayerGamePreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.genre')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.player')),
            ],
            options={
                'unique_together': {('player', 'genre')},
            },
        ),
    ]
