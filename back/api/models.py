from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()


class Music(models.Model):
    track_genre = models.CharField(max_length=50)
    track_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    cover_path = models.CharField(max_length=200)
    popularity = models.IntegerField()
    preview_url = models.CharField(max_length=200)
