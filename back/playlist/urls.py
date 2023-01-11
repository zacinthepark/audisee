from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.track_list),
    path('tracks/<int:track_pk>/', views.track_change),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_change),
    path('member/tracks/<int:member_pk>/', views.member_track_list),
    path('member/movies/<int:member_pk>/', views.member_movie_list),
]
