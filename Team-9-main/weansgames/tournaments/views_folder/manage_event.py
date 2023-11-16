from django.shortcuts import render, get_object_or_404
from tournaments.models import User, Volunteer, Event
from tournaments.forms import CreateEventForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def manage_event(request, id):
    registered = False
    if request.method == "POST":
        found_event = Event.objects.get(id=id)
        event_form = CreateEventForm(request.POST, instance=found_event)
        if event_form.is_valid():
            child = event_form.save()
            registered = True
        form = None

        return redirect(reverse("tournaments:home"))
    else:
        event_form = CreateEventForm(instance = Event.objects.get(id = id))
    return render(request, 'weansgames/manage_event.html', context = {
        "event_form": event_form,
        "registered": registered,
        "id": id,
    })
 