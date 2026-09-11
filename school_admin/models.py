from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name='school_admin')
    admin_id = models.CharField(db_column='Admin_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.BigIntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'