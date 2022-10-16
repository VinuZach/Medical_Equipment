from django.shortcuts import render
from .models import *
from django.contrib.auth import login, authenticate, logout

# Create your views here.

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


def displayHome(request):
    return render(request, 'HomePage.html', {"menuLists": menuItems})


def displayGalleryPage(request):
    gallerySections = GallerySections.objects.all()
    return render(request, 'GalleryPage.html', {"gallerySections": gallerySections})


def displayStudentRegistration(request):
    if request.method == "POST":
        try:
            joing_date = request.POST.get("joing_date")
            joing_time = request.POST.get("joing_time")
            stu_date = request.POST.get("stu_date")
            stud_name = request.POST.get("stud_name")
            ma_occupation = request.POST.get("ma_occupation")
            mother_name = request.POST.get("mother_name")
            father_name = request.POST.get("father_name")
            fa_occupation = request.POST.get("fa_occupation")
            gender = request.POST.get("gender")
            caste_category = request.POST.get("category")
            P_address = request.POST.get("P_address")
            Per_address = request.POST.get("Per_address")
            caste = request.POST.get("caste")
            religion = request.POST.get("religion")
            m_tongue = request.POST.get("m_tongue")
            m_phone = request.POST.get("m_phone")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            b_group = request.POST.get("b_group")
            category_qual = request.POST.get("category_qual")
            pass_year = request.POST.get("pass_year")
            last_school = request.POST.get("last_school")
            selected_course = request.POST.get("selected_course")
            fee_struct = request.POST.get("fee_struct")
            pay_class = request.POST.get("pay_class")
            extra_pay = request.POST.get("extra_pay")

            print(joing_date)
            print(joing_time)
            print(stud_name)
            print(stu_date)
            print(mother_name)
            print(ma_occupation)
            print(fa_occupation)
            print(father_name)
            print(gender)
            print(caste_category)
            print(P_address)
            print(Per_address)
            print(caste)
            print(religion)
            print(m_tongue)
            print(phone)
            print(m_phone)
            print(email)
            print(b_group)
            print(last_school)
            print(category_qual)
            print(pass_year)
            print(selected_course)
            print(fee_struct)
            print(extra_pay)
            print(pay_class)
            uploaded_file = request.FILES['document']
            StudentDetails.objects.create(joining_date=joing_date, joining_time=joing_time, student_name=stud_name,
                                          student_DOB=stu_date, student_mother_name=mother_name,
                                          student_caste_category=caste_category,
                                          student_mother_occup=ma_occupation, student_father_name=father_name,
                                          student_father_occup=fa_occupation, student_gender=gender,
                                          presentAddress=P_address, permanentAddress=Per_address, caste=caste,
                                          religion=religion, mother_tongue=m_tongue, phone=phone, mobileNumber=m_phone,
                                          emailId=email, blood_group=b_group, last_attended_school=last_school,
                                          last_attended_school_qual=category_qual, year_of_passing=pass_year,
                                          selectedCourse=selected_course, fee_schedule=fee_struct, tobe_payed=extra_pay,
                                          tobe_Qual=pay_class, imageData=uploaded_file)
        except Exception as e:
            print(e)
    return render(request, 'RegistrationPage.html', {"menuLists": menuItems})


def uploadNews_admin(request):
    print("uploadNews_admin")
    if request.method == "POST":
        try:
            text = request.POST.get("headerData")
            uploaded_file = request.FILES['document']
            print(uploaded_file.name)
            LatestNewsAndUpdates.objects.create(newsHeading=text, imageData=uploaded_file)
            print(text)
        except Exception as e:
            print(e)
    return render(request, 'admin/admin_upload_news.html', {})


def adminLogin(request):
    user = None
    error = ""
    if request.user.is_authenticated:
        user = request.user
    if request.method == "POST":
        userName = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, email=userName, password=password)
        print(user)
        if user is not None:
            login(request, user)
        else:
            print("user is not authenticated")
            error = "Invalid Account Details"
    return render(request, 'admin/admin_home.html', {"user": user, "error": error})


def displayStudents(request, offset):
    if request.method == "POST":
        print("inside")
        studentDetails = request.POST.get("studentID")
        print(studentDetails)
        studentDetails = StudentDetails.objects.get(id=studentDetails)
        return render(request, 'admin/individualStudent_admin.html', {"studentDetails": studentDetails})
    else:
        print(offset)
        index = 1
        if offset is None:
            index = 1
            offset = 0
        else:
            if offset != 0:
                index = (offset / 10) + 1
        studentDetails = StudentDetails.objects.all()[offset:10]
        prevOffset = offset - 10
        if prevOffset < 0:
            prevOffset = 0
        offset += 10

        return render(request, 'admin/StudentDetails_admin.html',
                      {"studentDetails": studentDetails, "nextOffset": offset, "prevOffset": prevOffset,
                       "index": int(index)})


def logout_admin(request):
    logout(request)
    print("logout")
    return render(request, 'admin/Logout_admin.html')


def uploadGallery_admin(request):
    print("health_admin_gallery")

    gallerySections = GallerySections.objects.all()
    if request.method == "POST":

        try:
            text = request.POST.get("headerData")
            sectionId = request.POST.get("sectionId")
            uploaded_file = request.FILES['document']
            print(sectionId)
            if sectionId == "New":
                selectedSection = GallerySections.objects.create(galleryTitle=text)
            else:
                selectedSection = GallerySections.objects.get(id=sectionId)
            GalleryImages.objects.create(gallery_section=selectedSection, imageData=uploaded_file)

        except Exception as e:
            print(e)
    return render(request, 'admin/admin_apload_gallery.html', {"gallerySections": gallerySections})
