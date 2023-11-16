from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from tournaments.forms import AddChildForm, VolunteerForm
from django.urls import reverse
from django.shortcuts import redirect
@staff_member_required
def add_child(request):
    registered = False
    if request.method == "POST":
        player_form = VolunteerForm(request.POST)
        child_form = AddChildForm(request.POST)
        if player_form.is_valid() and child_form.is_valid():
            child = child_form.save(commit=False)
            player = player_form.save()
            child.player = player
            child.availability = True
            child.save()
            registered = True
            return redirect(reverse("tournaments:home"))
    else:
        player_form = VolunteerForm()
        child_form = AddChildForm()
    return render(request, 'weansgames/add_child.html', context = {
        "player_form": player_form,
        "child_form": child_form,
        "registered": registered
    })
 