from rest_framework import viewsets
from www.models import Lyrics
from . import serializers

class LyricsViewSet(viewsets.ModelViewSet):
  queryset = Lyrics.objects.all()
  serializer_class = serializers.LyricsSerializer

