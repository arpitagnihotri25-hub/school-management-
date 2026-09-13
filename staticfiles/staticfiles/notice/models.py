from django.db import models

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word. # Field name made lowercase.
    post_date = models.DateField(db_column='Post_Date', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    post_by_name = models.CharField(db_column='Post_by_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    post_by_id = models.CharField(db_column='Post_by_ID',max_length=20,blank=True,null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notice'