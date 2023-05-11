from rest_framework import serializers
from .models import Genre, Album, Song, Artist

class GenreSer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ["name"]
        
class AlbumSer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    
    class Meta:
        model = Album
        fields = ["title", "genre", "release_date"]
        
class ArtistSer(serializers.ModelSerializer):
    albums = AlbumSer(many=True)
    
    class Meta:
        model = Artist
        fields = ["name", "albums"]
    
class SongSer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()
    
    class Meta:
        model = Song
        fields = ["album", "title", "length", "track_number"]
