from django.shortcuts import render

def index(request):
    # Placeholder movies
    movies = [
        {"id": 1, "title": "The Shawshank Redemption", "image_url": "/static/home/shawshank.jpg", "rating": 9.3},
        {"id": 2, "title": "The Godfather", "image_url": "/static/home/thegodfather.jpg", "rating": 9.0},
        {"id": 3, "title": "Schindler's List", "image_url": "/static/home/schindler.jpg", "rating": 9.0},
    ]
    return render(request, 'home/index.html', {"movies": movies})
