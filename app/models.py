from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Album(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()

class Artist(models.Model):
    name = models.CharField(max_length=50)
    albums = models.ManyToManyField(Album)
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    length = models.BigIntegerField()
    track_number = models.BigIntegerField()