from rest_framework import serializers
from .models import MyTrack, MyMovie

class MyTrackSerialzer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = MyTrack
        fields = '__all__'
        read_only_fields = ('user',)

class MyMovieSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = MyMovie
        fields = '__all__'
        read_only_fields = ('user',)

class MyTrackListSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = MyTrack
        fields = ('id', 'track_genre', 'track_name', 'artist_name', 'album_name', 'cover_path', 'preview_url',)

class MyMovieListSerialzer(serializers.ModelSerializer):

    class Meta:
        model = MyMovie
        fields = ('id', 'title', 'poster_path',)
