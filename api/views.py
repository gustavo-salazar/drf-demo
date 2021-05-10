from rest_framework import viewsets
from www.models import Artist
from . import serializers

class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = serializers.ArtistSerializer
