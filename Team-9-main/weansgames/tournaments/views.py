from tournaments.views_folder import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

def about(request):
    return render(request, "weansgames/about.html")

@login_required
def auth_logout(request):
    logout(request)
    return redirect(reverse("tournaments:home"))

def contact(request):
    return render(request,"weansgames/contact.html")
