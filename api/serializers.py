from rest_framework import serializers
from www.models import Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):
  artist = serializers.StringRelatedField(many=False)
  class Meta:
    model = Song
    fields = ['id', 'name', 'lyrics', 'artist' ]
