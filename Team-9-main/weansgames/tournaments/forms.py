from django import forms
from django.contrib.auth.models import User
from datetime import date
import datetime
from tournaments.models import Player, Kid, Game, Genre, Event, GameResult, Volunteer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(max_length= 200,required=True)
    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

    class Meta:
        model = User
        fields = {'username', 'password'}

class VolunteerForm(forms.ModelForm):
    name = forms.CharField()
    surname = forms.CharField()

    class Meta:
        model = Player
        fields = ('name', 'surname')

class AddChildForm(forms.ModelForm):
    age = forms.IntegerField()
    class Meta:
        model = Kid
        fields = (('age',"favourite_genre"))

class CreateEventForm(forms.ModelForm):
    startDate = forms.DateTimeField(initial=datetime.datetime.today, label='Start Time`',
                                    widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)
    endDate = forms.DateTimeField(initial=datetime.datetime.today, label='End Time',
                                    widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)

    class Meta:
        model = Event
        fields = ('name', 'startDate', 'endDate', 'game', 'players')

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'quantity', 'description', 'genre')

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
