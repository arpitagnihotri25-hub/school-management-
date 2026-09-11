from django.contrib import admin

from classteacher.models import Classteacher

class classteacher(admin.ModelAdmin):
    list_display=('class_number','section','class_teacher_name','staff_id')

admin.site.register(Classteacher,classteacher)