from django.contrib import admin

from feesstatus.models import FeesStatus

class feesstatus(admin.ModelAdmin):
    list_display=('status_id','admission_no','student_name','class_field','section','deposit_date','deposit_amount')

admin.site.register(FeesStatus,feesstatus)