from django.contrib import admin

from notice.models import Notice

class notice(admin.ModelAdmin):
    list_display=('notice_id','class_field','post_date','title','description','post_by_name','post_by_id')

admin.site.register(Notice,notice)