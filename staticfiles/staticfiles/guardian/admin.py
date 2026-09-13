from django.contrib import admin

from guardian.models import Guardian

class guardian(admin.ModelAdmin):
    list_display=('admission_no','name','guardian_id','email','contact','relation','occupation','address')

admin.site.register(Guardian,guardian)