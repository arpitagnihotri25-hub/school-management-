from django.contrib import admin

from homework.models import Homework

class homework(admin.ModelAdmin):
    list_display=('homework_id','class_field','section','post_date','subject','description','post_by_name','post_by_id')

admin.site.register(Homework,homework)