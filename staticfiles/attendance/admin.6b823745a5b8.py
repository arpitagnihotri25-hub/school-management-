from django.contrib import admin

from attendance.models import Attendance

class attendance(admin.ModelAdmin):
    list_display=('attendance_id','admission_no','student_name','class_field','section','date','status')

admin.site.register(Attendance,attendance)