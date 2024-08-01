from rest_framework import serializers
from .models import Song, Album, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistSerializer_new(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name')

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = '__all__'

class AlbumSerializer_new(serializers.ModelSerializer):
    artist = ArtistSerializer_new()
    class Meta:
        model = Album
        fields = ['title', 'artist', 'image']

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = '__all__'

class SongSerializer_new(serializers.ModelSerializer):
    album = AlbumSerializer_new()
    class Meta:
        model = Song
        fields = ['title', 'album', 'image']
