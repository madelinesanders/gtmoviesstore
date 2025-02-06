from django.db import models
from django.contrib.auth.models import User #check to see if this updates w team
from home.models import Movie  #check to see if this updates w madeline

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #foreignkey to user
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  #rating option
    comment = models.TextField()  #review left by user
    created_at = models.DateTimeField(auto_now_add=True)  #time review was made

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"
