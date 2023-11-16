from django.db import models
from django.contrib.auth.models import User


DESCRIPTION_LENGTH = 1024
NAME_LENGTH = 64
SURNAME_LENGTH = 64
GAME_NAME_LENGTH = 64
GENRE_NAME_LENGTH = 64


class Player(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    surname = models.CharField(max_length=SURNAME_LENGTH)
    
    def __str__(self):
        return self.name + " " + self.surname


class Genre(models.Model):
    name = models.CharField(max_length=GENRE_NAME_LENGTH)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=GAME_NAME_LENGTH)
    quantity = models.IntegerField()
    description = models.CharField(max_length=DESCRIPTION_LENGTH)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    NURSE = "N"
    DOCTOR = "D"
    ADMIN = "A"
    ROLE_CHOICES = [
        (NURSE, "Nurse"),
        (DOCTOR, "Doctor"),
        (ADMIN, "Admin")
    ]
    role_choice = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default="N"
    )

    surname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    availability = models.BooleanField()
    def __str__(self):
        return self.firstname + " " + self.surname

class Event(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    staff = models.ManyToManyField(Staff)
    online = models.BooleanField(default=False)
    max_no_of_players = models.IntegerField(default=0)


class GameResult(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="Player_two_set")
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="Player_one_set")
    player_one_won = models.BooleanField()


class Kid(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(blank=True)
    availability = models.BooleanField()
    favourite_genre = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.player.name + " " + self.player.surname


class Volunteer(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isVerified = models.BooleanField()

    def __str__(self):
        return self.player.name + " " + self.player.surname


class PlayerGamePreferences(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'genre',)