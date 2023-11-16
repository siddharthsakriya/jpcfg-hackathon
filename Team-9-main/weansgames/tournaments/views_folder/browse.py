from django.shortcuts import render
from django.urls import reverse
from tournaments.models import Event
from django.contrib.auth.decorators import login_required


@login_required
def browse(request):
    return render(request, "weansgames/browse.html", {
        "events":Event.objects.all()
    })

