from django.db import models

class Homework(models.Model):
    homework_id = models.AutoField(primary_key=True)
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True, choices=[("Class 9th", "Class 9th"), ("Class 10th", "Class 10th"), ("Class 11th", "Class 11th"), ("Class 12th", "Class 12th")])  # Field name made lowercase. Field renamed because it was a Python reserved word.
    section = models.CharField(db_column='Section', max_length=20, blank=True, null=True, choices=[("A", "A"), ("B", "B"), ("C", "C")])  # Field name made lowercase.
    post_date = models.DateField(db_column='Post_date', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    post_by_name = models.CharField(db_column='Post_by_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    post_by_id = models.CharField(db_column='Post_by_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'homework'
