from django.shortcuts import render
from tournaments.models import Game
from django.contrib.admin.views.decorators import staff_member_required
from tournaments.forms import GameForm
from django.urls import reverse
from django.shortcuts import redirect
@staff_member_required
def add_game(request):
    registered = False
    if request.method == "POST":
        game_form = GameForm(request.POST)
        if game_form.is_valid() and not Game.objects.filter(name=request.POST['name']).exists():
            game = game_form.save()
            game.save()
            registered = True
            return redirect(reverse("tournaments:home"))
    else:
        game_form = GameForm()

    return render(request, 'weansgames/add_game.html', context = {
        "game_form": game_form,
        "registered": registered
    })
 