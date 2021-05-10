from django.http import HttpResponse
from www.models import Song

def index(request):
  return HttpResponse(
    f"This Lyrics website has {Song.objects.count()} songs.")
