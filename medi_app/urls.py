from django.urls import path, include
from .views import *
from .ApiCalls import *

urlpatterns = [
    path("", displayHome),

    path("gallery_page", displayGalleryPage),
    path("student_registration", displayStudentRegistration),
    path("about_us", displayAboutUs),
    path("campus_and_classrooms", displayClassesAndCampus),
    path("laboratory_page", displayLaboratory),
    path("digital_classroom", displayClassRoom)
]
# admin pages
urlpatterns += [
    path("health_admin", uploadNews_admin),
    path("health_admin_gallery", uploadGallery_admin),
    path("logout_admin", logout_admin),
    path("health_admin_studentDetails/<int:offset>", displayStudents),
    path("adminHome", adminLogin, name="adminHome"),

]

# api links
urlpatterns += [
    path("getAllNewsList", getNewsAndHeaders_api),
    path("getCourseDetails", getCourseDetails),
    path("getGallerySections", getGallerySections),
    path("getGalleryImages", getGalleryImages),
]
