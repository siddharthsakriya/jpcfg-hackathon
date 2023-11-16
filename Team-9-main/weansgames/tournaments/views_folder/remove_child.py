from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from tournaments.models import Kid

@staff_member_required
def remove_child(request):
    
    if request.method == "POST":
        kid = Kid.objects.filter(player__name = request.POST["name"], player__surname = request.POST["surname"], age = request.POST["age"])
        if kid.exists():
            kid[0].delete()

    return render(request, 'weansgames/remove_child.html', context = {
        "child_list": Kid.objects.all()
    })
 