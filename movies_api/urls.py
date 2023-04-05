from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from cinephile import settings
from movies.views import *

urlpatterns = [
]



from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'news', NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]