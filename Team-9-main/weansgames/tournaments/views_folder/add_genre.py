from django.shortcuts import render
from tournaments.models import Genre
from tournaments.forms import GenreForm
from django.urls import reverse
from django.shortcuts import redirect
def add_genre(request):
    registered = False
    if request.method == "POST":
        genre_form = GenreForm(request.POST)
        if genre_form.is_valid() and not Genre.objects.filter(name=request.POST['name']).exists():
            genre = genre_form.save()
            genre.save()
            registered = True
            return redirect(reverse("tournaments:home"))
    else:
        genre_form = GenreForm()

    return render(request, 'weansgames/add_genre.html', context = {
        "genre_form": genre_form,
        "registered": registered
    })
 