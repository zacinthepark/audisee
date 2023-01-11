from django.db import models
from django.conf import settings

# Create your models here.

class MyTrack(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tracks")
    # music = models.ForeignKey('api.Music', on_delete=models.CASCADE)
    track_genre = models.CharField(max_length=50)
    track_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    cover_path = models.CharField(max_length=200)
    preview_url = models.CharField(max_length=200)

class MyMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movies")
    # movie = models.ForeignKey('api.Movie', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
