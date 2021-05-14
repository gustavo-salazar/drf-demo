from rest_framework import serializers
from www.models import Lyrics

class LyricsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lyrics
    fields = ['id', 'artist', 'name', 'lyrics']

