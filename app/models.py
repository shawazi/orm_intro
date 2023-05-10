from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    # on_delete=models.PROTECT <--- prevents deletion if that genre still contains albums
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=50)
    albums = models.ManyToManyField(Album)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    length = models.BigIntegerField()
    track_number = models.BigIntegerField()
    
    def __str__(self):
        return self.title + " from album: " + self.album