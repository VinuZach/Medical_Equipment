from django.urls import path, include
from .views import *
from .ApiCalls import *

urlpatterns = [
    path("", displayHome),
    path("health_admin", uploadNews_admin),
    path("gallery_page", displayGalleryPage)
]

# api links
urlpatterns += [
    path("getAllNewsList", getNewsAndHeaders_api),
    path("getCourseDetails", getCourseDetails),
    path("getGallerySections", getGallerySections),
    path("getGalleryImages", getGalleryImages),
]
