from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm, ReviewEditForm
from home.models import Movie
from django.contrib.auth.decorators import login_required

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()  # Fetch all reviews for the movie
    review_form = None

    # Handle new review form submission
    if request.method == 'POST':
        if request.user.is_authenticated:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.movie = movie
                new_review.user = request.user
                new_review.save()
                return redirect('movie_detail', movie_id=movie.id)
        else:
            return redirect('login')  # Redirect to login if the user is not authenticated

    else:
        review_form = ReviewForm()

    return render(request, 'movie_information/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form,
    })
def index(request):
    # Fetch all movies to display on the index page
    movies = Movie.objects.all()
    return render(request, 'movie_information/index.html', {'movies': movies})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    movie = review.movie
    if request.method == 'POST':
        form = ReviewEditForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=review.movie.id)
    else:
        form = ReviewEditForm(instance=review)
    return render(request, 'movie_information/edit_review.html', {
        'form': form,  # The form object
        'movie': movie  # The related movie object)
    })
