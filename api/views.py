from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from www.models import Lyrics
from . import serializers

class LyricsViewSet(viewsets.ModelViewSet):
  queryset = Lyrics.objects.all()
  serializer_class = serializers.LyricsSerializer


class LyricsView(GenericAPIView):
  queryset = Lyrics.objects.all()
  serializer_class = serializers.LyricsSerializer

  def get(self, request, *args, **kwargs):
    try:
      artist = self.kwargs['artist']
      song = self.kwargs['song']
    except ValueError:
      raise Http404()
    q = self.get_queryset() \
      .filter(name=song) \
      .filter(artist=artist)
    if len(q) == 0:
      return Response(
        {"detail": f"The song [{song}] by [{artist}] was not found"}, 
        status=status.HTTP_404_NOT_FOUND
      )
    serializer = serializers.LyricsSerializer(q, many=True)
    return Response(serializer.data)

