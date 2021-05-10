from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name


class Song(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  lyrics = models.TextField()
