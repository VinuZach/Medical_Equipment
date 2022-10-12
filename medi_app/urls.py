from django.urls import path, include
from .views import *
from .ApiCalls import *

urlpatterns = [
    path("", displayHome),
    path("health_admin", uploadNews_admin)
]

# api links
urlpatterns += [
    path("getAllNewsList", getNewsAndHeaders_api),
    path("getCourseDetails", getCourseDetails),
]
