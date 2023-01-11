from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MyTrackListSerialzer, MyMovieListSerialzer, MyTrackSerialzer, MyMovieSerializer
from .models import MyTrack, MyMovie

# Create your views here.

@api_view(['GET', 'POST'])
def track_list(request):
    if request.method == 'GET':
        my_tracks = MyTrack.objects.filter(user=request.user)
        # my_tracks = get_list_or_404(MyTrack, user_id=user_pk)
        serializer = MyTrackListSerialzer(my_tracks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MyTrackSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def member_track_list(request, member_pk):
    if request.method == 'GET':
        user_id_list = []
        user_id_list.append(member_pk)
        tracks = MyTrack.objects.filter(user_id__in=user_id_list)
        serializer = MyTrackListSerialzer(tracks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def member_movie_list(request, member_pk):
    if request.method == 'GET':
        user_id_list = []
        user_id_list.append(member_pk)
        movies = MyMovie.objects.filter(user_id__in=user_id_list)
        serializer = MyMovieListSerialzer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        my_movies = MyMovie.objects.filter(user=request.user)
        # my_movies = get_list_or_404(MyMovie, user=user_pk)
        serializer = MyMovieListSerialzer(my_movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MyMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def track_change(request, track_pk):
    track = MyTrack.objects.get(pk=track_pk)

    if request.method == 'DELETE':
        track.delete()
        my_tracks = MyTrack.objects.filter(user=request.user)
        serializer = MyTrackListSerialzer(my_tracks, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
def movie_change(request, movie_pk):
    movie = MyMovie.objects.get(pk=movie_pk)

    if request.method == 'DELETE':
        movie.delete()
        my_movies = MyMovie.objects.filter(user=request.user)
        print(my_movies)
        serializer = MyMovieListSerialzer(my_movies, many=True)
        print(serializer)
        return Response(serializer.data)
