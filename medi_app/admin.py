from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(LatestNewsAndUpdates)
admin.site.register(CourseDetails)
admin.site.register(GalleryImages)
admin.site.register(GallerySections)
