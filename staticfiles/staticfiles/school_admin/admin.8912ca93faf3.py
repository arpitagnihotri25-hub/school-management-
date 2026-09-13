from django.contrib import admin

from school_admin.models import Admin

class school_admin(admin.ModelAdmin):
    list_display=('admin_id','name','email','contact')

admin.site.register(Admin,school_admin)

