from django.shortcuts import render
from tournaments.models import User, Volunteer
from tournaments.forms import UserForm, VolunteerForm
from django.urls import reverse
from django.shortcuts import redirect
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        player_form = VolunteerForm(request.POST)
        if user_form.is_valid() and player_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            player = player_form.save()
            volunteer = Volunteer()
            volunteer.user = user
            volunteer.player = player
            volunteer.isVerified = False
            volunteer.save()

            registered = True
            return redirect(reverse("tournaments:home"))
    else:
        user_form = UserForm()
        player_form = VolunteerForm()

    return render(request, 'weansgames/register.html', context = {
        "user_form": user_form,
        "player_form": player_form,
        "registered": registered
    })
 