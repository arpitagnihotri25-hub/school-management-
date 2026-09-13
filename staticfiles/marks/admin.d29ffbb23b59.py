from django.contrib import admin

from marks.models import Marks

class marks(admin.ModelAdmin):
    list_display=('marks_id','admission_no','student_name','term','class_field','section','subject','marks_obt','total_marks')

admin.site.register(Marks,marks)