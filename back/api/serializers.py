from rest_framework import serializers
from .models import Movie, Music, Genre

class GenreNameSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreNameSerialzer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
