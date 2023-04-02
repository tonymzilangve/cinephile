from django.urls import path

from feedback.views import *

urlpatterns = [
    path('reviews/', ShowReview.as_view(), name='show-review')
]
