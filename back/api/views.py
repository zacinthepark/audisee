from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404
from .serializers import MovieListSerializer, MusicListSerializer
from .models import Movie, Music

# Create your views here.

def mood_to_genre(mood):
    if mood == 'adventure':
        return [12, 14, 878]
    elif mood == 'animation':
        return [16, 10770]
    elif mood == 'humanism':
        return [18, 10751]
    elif mood == 'thrillers':
        return [27, 53]
    elif mood == 'actions':
        return [28, 10752]
    elif mood == 'comedy':
        return [35]
    elif mood == 'romance':
        return [10749]
    elif mood == 'history':
        return [36, 37, 99]
    elif mood == 'music':
        return [10402]
    elif mood == 'mysteries':
        return [9648, 80]

def mood_to_music(mood):
    if mood == 'adventure':
        return ['pop', 'holidays', 'drum-and-bass']
    elif mood == 'animation':
        return ['j-pop', 'anime', 'soundtracks']
    elif mood == 'humanism':
        return ['acoustic', 'piano', 'new-age']
    elif mood == 'thrillers':
        return ['rainy-day', 'classical', 'sad']
    elif mood == 'actions':
        return ['work-out', 'hip-hop', 'gospel']
    elif mood == 'comedy':
        return ['comedy', 'happy']
    elif mood == 'romance':
        return ['romance', 'r-n-b', 'pop']
    elif mood == 'history':
        return ['classical', 'country', 'road-trip']
    elif mood == 'music':
        return ['soundtracks', 'pop-film']
    elif mood == 'mysteries':
        return ['rainy-day', 'opera', 'sad']

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_list_by_mood(request, mood):
    if request.method == 'GET':
        genre_id_list = mood_to_genre(mood)
        movies = Movie.objects.filter(genres__in=genre_id_list).order_by('?')[:50]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    if request.method == 'GET':
        musics = get_list_or_404(Music)
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def music_list_by_mood(request, mood):
    if request.method == 'GET':
        music_genre_list = mood_to_music(mood)
        musics = Music.objects.filter(track_genre__in=music_genre_list).order_by('?')[:50]
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
