from django.shortcuts import render
from tournaments.models import User, Volunteer
from tournaments.forms import CreateEventForm
from send_email import push_email_notification
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.shortcuts import redirect
@staff_member_required
def create_event(request):
    registered = False
    if request.method == "POST":
        event_form = CreateEventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save()
            for player in event.players.all():
                volunteer = Volunteer.objects.filter(player=player)
                if volunteer.exists():
                    push_email_notification(volunteer[0].user.email, player.name, True)
                
            registered = True
            return redirect(reverse("tournaments:home"))
    else:
        event_form = CreateEventForm()
    return render(request, 'weansgames/create_event.html', context = {
        "event_form": event_form,
        "registered": registered
    })
 