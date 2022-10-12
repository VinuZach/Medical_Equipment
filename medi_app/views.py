from django.shortcuts import render
from .models import *

# Create your views here.

def displayHome(request):
    menuItems = {
        "menuList": [
            {
                "menu_title": "Home",
                "menu_subMenu": []
            },
            {
                "menu_title": "About us",
                "menu_subMenu": ["History", "Vision and Mission", "Aim and Objectives", "Specialties "]
            },
            {
                "menu_title": "Facilities",
                "menu_subMenu": ["Campus & classrooms", "Laboratory", "Digital classroom", "Surgical instrument lab ",
                                 "Transportation", "Girls' hostel facilities ", "Library & reading rooms"]
            },
            {
                "menu_title": "Students Corner",
                "menu_subMenu": ["Clubs", "Social Activities"]
            },
            {
                "menu_title": "Gallery",
                "menu_subMenu": ["Photos", "Videos"]
            }, {
                "menu_title": "Contact",
                "menu_subMenu": []
            }
        ]
    }

    return render(request, 'HomePage.html', {"menuLists": menuItems})


def uploadNews_admin(request):
    if request.method == "POST":
        try:
            text = request.POST.get("headerData")
            uploaded_file = request.FILES['document']
            print(uploaded_file.name)
            LatestNewsAndUpdates.objects.create(newsHeading=text,imageData=uploaded_file)
            print(text)
        except Exception as e:
            print(e)
    return render(request, 'admin/admin_upload_news.html', {})
