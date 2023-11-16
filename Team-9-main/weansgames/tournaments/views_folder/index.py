from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return render(request, "weansgames/admin_index.html")

    return render(request, "weansgames/index.html")
 