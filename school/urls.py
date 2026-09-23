"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('about/', views.about, name='about'),
    path('facilities/', views.facilities, name='facilities'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff/', views.staff, name='staff'),
    path('students/', views.students, name='students'),
    path('classes/', views.classes, name='classes'),
    path('attendance/', views.attendance, name='attendance'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    # path('marks/', views.marks, name='marks'),
    # path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('homework/', views.homework_function, name='homework'),
    path('notices/', views.notices, name='notices'),
    path('fees_details/', views.fees_details, name='fees_details'),
    path('fees_status/', views.fees_status, name='fees_status'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff_registration/', views.staff_registration, name='staff_registration'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('guardian_registration/', views.guardian_registration, name='guardian_registration'),
    path('guardian_dashboard/', views.guardian_dashboard, name='guardian_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]