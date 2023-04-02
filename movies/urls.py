from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from cinephile import settings
from .views import *

urlpatterns = [
    path('', FeedView.as_view(), name="feed"),
    path('<slug:movie_slug>/', show_movie_info, name='movie-info')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
