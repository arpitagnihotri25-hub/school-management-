from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login

def homepage(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        id=request.POST.get('id')
        password=request.POST.get('password')
        user=authenticate(request,username=id,password=password)
        if user:
            return redirect('/admin_dashboard/')
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def staff(request):
    return render(request,"staff.html")

def students(request):
    return render(request,"students.html")

def classes(request):
    return render(request,"classes.html")

def attendance(request):
    return render(request,"attendance.html")

def marks(request):
    return render(request,"marks.html")

def homework(request):
    return render(request,"homework.html")

def notices(request):
    return render(request,"notices.html")

def fees_details(request):
    return render(request,"fees_details.html")

def fees_status(request):
    return render(request,"fees_status.html")

def staff_dashboard(request):
    return render(request,"staff_dashboard.html")