from ast import Not
from datetime import date
from urllib import request

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

from staff.forms import register_staff
from student.forms import register_student
from guardian.forms import register_guardian
from feesstatus.forms import fees__status
from homework.forms import post_homework
from notice.forms import post_notice
from student.models import Student
from staff.models import Staff
from feesdetails.forms import fees__details
from feesdetails.models import FeeDetails
from classteacher.forms import ClassteacherForm
from classteacher.models import Classteacher
from classteacher.models import Classteacher
from attendance.models import Attendance
from homework.models import Homework
from guardian.models import Guardian
from notice.models import Notice
from feesstatus.models import FeesStatus

def homepage(request):
    return render(request,"index.html")

def userlogin(request):
    if request.method == "POST":
        id=request.POST.get('id')
        password=request.POST.get('password')
        if(id.startswith("ADM")):
            user=authenticate(request,username=id,password=password)
            print(id)
            print(password)
            if user:
                login(request,user)
                request.session['userid'] = id
                return redirect('/admin_dashboard/')
            else:
                return render(request,"login.html",{'message':'Enter Correct Password'})
        elif(id.startswith("STF")):
            user=authenticate(request,username=id,password=password)
            if user:
                login(request,user)
                request.session['userid'] = id
                return redirect('/staff_dashboard/')
            else:
                return render(request,"login.html",{'message':'Enter Correct Password'})
        elif(id.startswith("STD")):
            user=authenticate(request,username=id,password=password)
            if user:
                login(request,user)
                request.session['userid'] = id
                return redirect('/student_dashboard/')
            else:
                return render(request,"login.html",{'message':'Enter Correct Password'})
        elif(id.startswith("GDN")):
            user=authenticate(request,username=id,password=password)
            if user:
                login(request,user)
                request.session['userid'] = id
                return redirect('/guardian_dashboard/')
            else:
                return render(request,"login.html",{'message':'Enter Correct Password'})
        else:
            return render(request,"login.html",{'message':'Enter Correct id or number'})
    return render(request,"login.html")

def admin_dashboard(request):
    admin =request.user.school_admin
    return render(request,"admin_dashboard.html")

def staff(request):
    admin =request.user.school_admin
    staff_details=Staff.objects.all()
    return render(request,"staff.html",{'staff_details': staff_details})

def staff_registration(request):
    admin =request.user.school_admin
    fs=register_staff()
    if request.method == "POST":
        form=register_staff(request.POST)
        if(form.is_valid()):
            last_staff = Staff.objects.order_by('staff_id').last()
            if last_staff:
                last_num = int(last_staff.staff_id.replace("STF", ""))
                staff_id = f"STF{last_num + 1:04d}"
            else:
                staff_id = "STF0001"
            password=form.cleaned_data['name']+staff_id
            user=User.objects.create_user(username=staff_id,password=password)
            staff = form.save(commit=False)
            staff.user = user
            staff.staff_id = staff_id
            staff.save()
            form = register_staff()
            return render(request,"staff_registration.html",{'form': form,
                                                             'message':'Registered Successfully'})
        else:
            print(form.errors)
            return render(request,"staff_registration.html",{'form': form,
                                                             'message':'Not Registered'})
    return render(request,"staff_registration.html",{'form': fs})

def staff_dashboard(request):
    staff =request.user.staff
    staff_details=staff
    staff_role=staff.role
    return render(request,"staff_dashboard.html",{'staff_role':staff_role,
                                                  'staff_details':staff_details})

def students(request):
    userid = request.session.get('userid')
    student_details=Student.objects.all()
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        return render(request,"students.html",{'role':'Staff',
                                               'staff_role':staff_role,
                                               'student_details': student_details})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        return render(request,"students.html",{'role':'Admin',
                                               'student_details': student_details})
    return render(request,"students.html")

def student_registration(request):
    staff =request.user.staff
    staff_role=staff.role
    form=register_student()
    if request.method == "POST":
        form=register_student(request.POST)
        if(form.is_valid()):
            last_student = Student.objects.order_by('admission_no').last()
            if last_student:
                last_num = int(last_student.admission_no.replace("STD", ""))
                admission_no = f"STD{last_num + 1:04d}"
            else:
                admission_no = "STD0001"
            password=form.cleaned_data['name']+admission_no
            user=User.objects.create_user(username=admission_no,password=password)
            student = form.save(commit=False)
            student.user = user
            student.admission_no = admission_no
            student.save()
            form = register_student()
            return render(request,"student_registration.html",{'form': form,
                                                               'message':'Registered Successfully'
                                                               ,'staff_role':staff_role})
        else:
            print(form.errors)
            return render(request,"student_registration.html",{'form': form,
                                                               'message':'Not Registered',
                                                               'staff_role':staff_role})
    return render(request,"student_registration.html",{'form': form,
                                                       'staff_role':staff_role})

def student_dashboard(request):
    userid = request.session.get('userid')
    if(userid.startswith("STD")):
        student =request.user.student
        return render(request,"student_dashboard.html",{'role':'Student',
                                                     'student_details':student})
    elif(userid.startswith("GDN")):
        guardian =request.user.guardian
        student=guardian.admission_no
        return render(request,"student_dashboard.html",{'role':'Guardian',
                                                     'student_details':student})
    return render(request,"student_dashboard.html",{'student_details': student})

def guardian_registration(request):
    form=register_guardian()
    if request.method == "POST":
        form=register_guardian(request.POST)
        if(form.is_valid()):
            last_guardian = Guardian.objects.order_by('guardian_id').last()
            if last_guardian:
                last_num = int(last_guardian.guardian_id.replace("GDN", ""))
                guardian_id = f"GDN{last_num + 1:04d}"
            else:
                guardian_id = "GDN0001"
            password=form.cleaned_data['name']+guardian_id
            user=User.objects.create_user(username=guardian_id,password=password)
            guardian = form.save(commit=False)
            guardian.user = user
            guardian.guardian_id = guardian_id
            guardian.save()
            form = register_guardian()
            return render(request,"guardian_registration.html",{'form': form,
                                                                'message':'Registered Successfully'})
        else:
            print(form.errors)
            return render(request,"guardian_registration.html",{'form': form,
                                                                'message':'Not Registered'})
    return render(request,"guardian_registration.html",{'form': form})

def guardian_dashboard(request):
    guardian =request.user.guardian
    student=guardian.admission_no
    return render(request,"guardian_dashboard.html",{'guardian':guardian,
                                                     'student':student})

def classes(request):
    class_teacher_details=Classteacher.objects.all()
    userid = request.session.get('userid')
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        return render(request,"classes.html",{'role':'Staff',
                                              'staff_role':staff_role,
                                              'class_teacher_details': class_teacher_details})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        form=ClassteacherForm()
        if request.method == "POST":
            form=ClassteacherForm(request.POST)
            if(form.is_valid()):
                classteacher = form.save(commit=False)
                classteacher.save()
                form = ClassteacherForm()
                return render(request,"classes.html",{'role':'Admin',
                                                      'form': form,
                                                      'message':'Added Successfully',
                                                      'class_teacher_details': class_teacher_details})
            else:
                print(form.errors)
                return render(request,"classes.html",{'role':'Admin',
                                                      'form': form,
                                                      'message':'Not Added',
                                                      'class_teacher_details': class_teacher_details})
        return render(request,"classes.html",{'role':'Admin',
                                              'form': form,
                                              'class_teacher_details': class_teacher_details})
    return render(request,"classes.html",{'class_teacher_details': class_teacher_details})

def attendance(request):
    attendance_record=Attendance.objects.all()
    userid = request.session.get('userid')
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        return render(request,"attendance.html",{'role':'Staff',
                                                 'staff_role':staff_role,
                                                 'attendance_record':attendance_record})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        return render(request,"attendance.html",{'role':'Admin',
                                                 'attendance_record':attendance_record})
    elif(userid.startswith("STD")):
        student =request.user.student
        return render(request,"attendance.html",{'role':'Student',
                                                 'student':student,
                                                 'attendance_record':attendance_record})
    elif(userid.startswith("GDN")):
        guardian =request.user.guardian
        student=guardian.admission_no
        return render(request,"attendance.html",{'role':'Guardian',
                                                 'student':student,
                                                 'attendance_record':attendance_record})
    return render(request,"attendance.html")

def mark_attendance(request):
    userid = request.session.get('userid')
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        students = Student.objects.all().order_by('admission_no')
        class_teacher = Classteacher.objects.filter(staff_id=userid).first()
        if class_teacher:
            class_name = class_teacher.class_number
            section = class_teacher.section
            if request.method == "POST":
                for key, status in request.POST.items():
                    if key.startswith("attendance_"):
                        admission_no = key.replace("attendance_", "")
                        student = Student.objects.get(admission_no=admission_no)
                        Attendance.objects.create(
                admission_no=student,
                student_name=student.name,
                class_field=student.class_field.class_field,
                section=student.section,
                date=date.today(),
                status=status
            )
        return render(request,"mark_attendance.html",{'role':'Staff',
                                                      'class':class_name,
                                                      'section':section,
                                                      'staff_role':staff_role,
                                                      'students':students})
    return render(request,"mark_attendance.html")

# def marks(request):
#     userid = request.session.get('userid')
#     if(userid.startswith("STF")):
#         staff =request.user.staff
#         staff_role=staff.role
#         return render(request,"marks.html",{'role':'Staff','staff_role':staff_role})
#     elif(userid.startswith("ADM")):
#         admin =request.user.school_admin
#         return render(request,"marks.html",{'role':'Admin'})
#     return render(request,"marks.html")

# def upload_marks(request):
#     userid = request.session.get('userid')
#     if(userid.startswith("STF")):
#         staff =request.user.staff
#         staff_role=staff.role
        
#         return render(request,"upload_marks.html",{'role':'Staff','staff_role':staff_role})
#     return render(request,"upload_marks.html")

def homework_function(request):
    homework_details=Homework.objects.all()
    userid = request.session.get('userid')
    if(userid.startswith("STF")):  
        form = post_homework()
        staff =request.user.staff
        staff_role=staff.role
        if request.method == "POST":
            form = post_homework(request.POST)
            if form.is_valid():
                homework = form.save(commit=False)
                homework.post_date=date.today()
                homework.post_by_name=staff.name
                homework.post_by_id=staff.staff_id
                homework.subject=staff.subject
                homework.save()
                form = post_homework()
        return render(request,"homework.html",{'role':'Staff',
                                             'form': form,
                                             'staff_role':staff_role,
                                             'homework_details':homework_details})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        return render(request,"homework.html",{'role':'Admin',
                                               'homework_details':homework_details})
    elif(userid.startswith("STD")):
        student =request.user.student
        return render(request,"homework.html",{'role':'Student',
                                               'student':student,
                                               'homework_details':homework_details})
    elif(userid.startswith("GDN")):
        guardian =request.user.guardian
        student=guardian.admission_no
        return render(request,"homework.html",{'role':'Guardian',
                                                     'student':student,
                                                     'homework_details':homework_details})
    return render(request,"homework.html")

def notices(request):
    form = post_notice()
    notice_details=Notice.objects.all()
    userid = request.session.get('userid')
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        if request.method == "POST":
                    form = post_notice(request.POST)
                    if form.is_valid():
                        notice = form.save(commit=False)
                        notice.post_date=date.today()
                        notice.post_by_name=staff.name
                        notice.post_by_id=staff.staff_id
                        notice.save()
                        form = post_notice()
                    else:
                        print(form.errors)
        return render(request,"notices.html",{'role':'Staff',
                                             'form': form,
                                             'staff_role':staff_role,
                                             'notice_details':notice_details})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        if request.method == "POST":
            form = post_notice(request.POST)
            if form.is_valid():
                notice = form.save(commit=False)
                notice.post_date=date.today()
                notice.post_by_name=admin.name
                notice.post_by_id=admin.admin_id
                notice.save()
                form = post_notice()
        return render(request,"notices.html",{'role':'Admin',
                                             'form': form,
                                             'notice_details':notice_details})
    elif(userid.startswith("STD")):
        student =request.user.student
        return render(request,"notices.html",{'role':'Student',
                                                   'student':student,
                                                   'notice_details':notice_details})
    elif(userid.startswith("GDN")):
        guardian =request.user.guardian
        student=guardian.admission_no
        return render(request,"notices.html",{'role':'Guardian',
                                               'student':student,
                                               'notice_details':notice_details}) 
    return render(request,"notices.html",{'form': form})

def fees_details(request):
    fees=FeeDetails.objects.all()
    userid = request.session.get('userid')
    form=fees__details()
    if(userid.startswith("STF")):
        staff =request.user.staff
        staff_role=staff.role
        return render(request,"fees_details.html",{'role':'Staff',
                                                   'staff_role':staff_role,
                                                   'fees': fees})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        form=fees__details()
        form = fees__details(request.POST)
        if form.is_valid():
            fees_details = form.save(commit=False)
            fees_details.save()
            form = fees__details()
            return render(request,"fees_details.html",{'role':'Admin',
                                                       'form':form,
                                                       'fees': fees,
                                                       'message':'Added'})
        else:
            print(form.errors)
            return render(request,"fees_details.html",{'role':'Admin',
                                                       'form':form,
                                                       'fees': fees,
                                                       'message':'Not Added'})
    return render(request,"fees_details.html",{'fees': fees})

def fees_status(request):
    fees_record=FeesStatus.objects.all()
    userid = request.session.get('userid')
    if(userid.startswith("STF")):
        form = fees__status()
        staff =request.user.staff
        staff_role=staff.role
        if request.method == "POST":
            form = fees__status(request.POST)
            if form.is_valid():
                feesstatus = form.save(commit=False)
                feesstatus.save()
                form = fees__status()
        return render(request,"fees_status.html",{'role':'Staff',
                                                  'form': form,
                                                  'staff_role': staff_role,
                                                  'fees_record': fees_record})
    elif(userid.startswith("ADM")):
        admin =request.user.school_admin
        return render(request,"fees_status.html",{'role':'Admin',
                                                  'fees_record':fees_record})
    elif(userid.startswith("STD")):
        student =request.user.student
        return render(request,"fees_status.html",{'role':'Student',
                                                  'student':student,
                                                  'fees_record':fees_record})
    elif(userid.startswith("GDN")):
            guardian =request.user.guardian
            student=guardian.admission_no
            return render(request,"fees_status.html",{'role':'Guardian',
                                                      'student':student,
                                                      'fees_record':fees_record})
    return render(request,"fees_status.html")

def userlogout(request):
    logout(request)
    redirect('/login/')
    return render(request,"logout.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")