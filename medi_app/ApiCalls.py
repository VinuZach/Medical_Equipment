from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
from .serializers import *


@api_view(['GET'])
def getNewsAndHeaders_api(request):
    newsList = LatestNewsAndUpdates.objects.all()[:5]
    return JsonResponse({"newsList": NewsDataSerializer(newsList, many=True).data}, safe=False)


@api_view(['GET'])
def getCourseDetails(request):
    courseDetails = CourseDetails.objects.all()
    return JsonResponse({"courseDetailsList": CourseDataSerializer(courseDetails, many=True).data}, safe=False)


@api_view(['GET'])
def getGallerySections(request):
    gallerySections = GallerySections.objects.all()
    return JsonResponse({"courseDetailsList": GallerySectionsSerializer(gallerySections, many=True).data}, safe=False)


@api_view(['GET'])
def getGalleryImages(request):
    print(request.GET.get("index"))
    index = request.GET.get("index")
    if index == "0":
        print("inside 0")
        galleryImages = GalleryImages.objects.all()
    else:
        galleryImages = GalleryImages.objects.filter(id=index)
    return JsonResponse({"galleryImages": GalleryImagesSerializer(galleryImages, many=True).data}, safe=False)
