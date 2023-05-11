from rest_framework import serializers
from .models import Genre, Album, Song, Artist

class GenreSer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ["id", "name"]
        
class AlbumSer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField() # not available for post method
    genre_id = serializers.IntegerField(write_only=True) # not available for get method
    records = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Album
        fields = ["id", "genre_id", "title", "genre", "release_date", "records"]
        
class ArtistSer(serializers.ModelSerializer):
    # albums = AlbumSer(many=True)
    
    class Meta:
        model = Artist
        fields = ["id", "name", "albums"]
    
class SongSer(serializers.ModelSerializer):
    album = serializers.StringRelatedField(many=True)
    album_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Song
        fields = ["id", "album", "title", "length", "track_number"]
