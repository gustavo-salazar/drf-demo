from django.db import models

class Lyrics(models.Model):
  artist = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  lyrics = models.TextField()
