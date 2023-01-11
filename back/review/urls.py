from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/', views.movie_review_list),
]
