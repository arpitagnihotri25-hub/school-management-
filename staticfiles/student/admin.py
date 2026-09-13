from django.contrib import admin

from student.models import Student

class student(admin.ModelAdmin):
    list_display=('admission_no','name','class_field','section','father_name','mother_name','father_occupation','mother_occupation','father_contact','mother_contact','dob','address','gender','house','blood_group','mode_of_transport')

admin.site.register(Student,student)