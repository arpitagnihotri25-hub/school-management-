from django.contrib import admin

from feesdetails.models import FeeDetails

class feedetails(admin.ModelAdmin):
    list_display=('class_field','amount')

admin.site.register(FeeDetails,feedetails)