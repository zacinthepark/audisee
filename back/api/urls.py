from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<str:mood>/', views.movie_list_by_mood),
    path('musics/', views.music_list),
    path('musics/<str:mood>/', views.music_list_by_mood),
]
