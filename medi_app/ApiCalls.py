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
