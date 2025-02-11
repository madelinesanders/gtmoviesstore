from django.shortcuts import render
from .models import Movie

def index(request):
    query = request.GET.get("q", "")
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, "home/index.html", {"movies": movies, "query": query})
