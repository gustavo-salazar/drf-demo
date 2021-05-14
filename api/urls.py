from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lyrics', views.LyricsViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path(r'lyrics/<str:artist>/<str:song>', views.LyricsView.as_view())
]
