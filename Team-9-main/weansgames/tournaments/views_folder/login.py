from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from tournaments.forms import LoginForm

def login(request):
    user_form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse("tournaments:home"))
            else:
                return HttpResponse("Your WeansGames account is disabled")
        else:
            return render(request, 'weansgames/login.html', {'user_form':user_form, 'invalid_login':True})
    else:
        return render(request, 'weansgames/login.html', {'user_form': user_form})

 