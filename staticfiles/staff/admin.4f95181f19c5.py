from django.contrib import admin

from staff.models import Staff

class staff(admin.ModelAdmin):
    list_display=('staff_id','name','email','contact','qualifications','experience','subject','class_field','address','gender','role')

admin.site.register(Staff,staff)