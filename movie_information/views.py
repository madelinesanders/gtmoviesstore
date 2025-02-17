from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Movie
movies = [
    {
        'id': 1, 'name': 'Inception', 'price': 12,
        'description': 'A mind-bending heist thriller.'
    },
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world and the battle for resources.'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gothams vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 11,
        'description': 'A love story set against the backdrop of the sinking Titanic.',
    },
]
def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movie_information/index.html',
                  {'template_data': template_data})

def movie_detail(request, movie_id):
    # Use get_object_or_404 to fetch the movie or return a 404 if not found
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_information/movie_detail.html', {'movie': movie})