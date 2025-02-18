from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movie_information.index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
]