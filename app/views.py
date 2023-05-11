from django.shortcuts import HttpResponse
from .models import Song, Album, Artist, Genre
from .serializers import SongSer, AlbumSer, ArtistSer, GenreSer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class GenreView(ListCreateAPIView):
    serializer_class = GenreSer
    queryset = Genre.objects.all()

class GenreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSer
    queryset = Genre.objects.all()

class ArtistView(ListCreateAPIView):
    serializer_class = ArtistSer
    queryset = Artist.objects.all()

class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSer
    queryset = Artist.objects.all()

class AlbumView(ListCreateAPIView):
    serializer_class = AlbumSer
    queryset = Album.objects.all()

class AlbumDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSer
    queryset = Album.objects.all()
    
class SongView(ListCreateAPIView):
    serializer_class = ArtistSer
    queryset = Artist.objects.all()

class SongDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSer
    queryset = Song.objects.all()