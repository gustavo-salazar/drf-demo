from django.http import HttpResponse
from www.models import Lyrics

def index(request):
  return HttpResponse(
    f"This Lyrics website has {Lyrics.objects.count()} songs.")

