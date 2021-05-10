from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from www.models import Artist, Song
from . import serializers

class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = serializers.ArtistSerializer


class SongView(GenericAPIView):
  queryset = Song.objects.all()
  serializer_class = serializers.SongSerializer

  def get(self, request, *args, **kwargs):
    try:
      artist = self.kwargs['artist']
      song = self.kwargs['song']
    except ValueError:
      raise Http404()
    q = self.get_queryset() \
      .filter(name=song) \
      .filter(artist__name=artist)
    if len(q) == 0:
      return Response(
        {"detail": f"The song [{song}] by [{artist}] was not found"}, 
        status=status.HTTP_404_NOT_FOUND
      )
    serializer = serializers.SongSerializer(q, many=True)
    return Response(serializer.data)
