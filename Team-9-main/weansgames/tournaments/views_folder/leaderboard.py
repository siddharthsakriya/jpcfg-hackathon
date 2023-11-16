from django.shortcuts import render

def leaderboard(request):
    if request.user.is_authenticated:
        return render(request, "weansgames/leaderboard.html")