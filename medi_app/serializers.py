from rest_framework import serializers
from .models import *


class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNewsAndUpdates
        fields = ["newsHeading", "imageData"]


class CourseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetails
        fields = ["courseName", "imageData", "duration"]


class GallerySectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySections
        fields = ["galleryTitle", 'id']


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ["imageData"]
