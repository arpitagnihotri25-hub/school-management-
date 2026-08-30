from django.db import models

class Admin(models.Model):
    admin_id = models.CharField(db_column='Admin_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.BigIntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'