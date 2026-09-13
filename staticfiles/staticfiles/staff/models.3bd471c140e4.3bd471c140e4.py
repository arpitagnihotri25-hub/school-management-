from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    staff_id = models.CharField(db_column='Staff_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.BigIntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    qualifications = models.CharField(db_column='Qualifications', max_length=100, blank=True, null=True)  # Field name made lowercase.
    experience = models.CharField(db_column='Experience', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=20, blank=True, null=True, choices=[("Physics", "Physics"), 
                            ("Chemistry", "Chemistry"), ("Biology", "Biology"), ("Mathematics", "Mathematics"), 
                            ("Computer Science", "Computer Science"), ("English", "English")])  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=20, blank=True, null=True, choices=[("Class 9th and 10th", "Class 9th and 10th"), ("Class 11th and 12th", "Class 11th and 12th")])  # Field name made lowercase. Field renamed because it was a Python reserved word.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True, choices=[("Male", "Male"), ("Female", "Female"), ("Others", "Others")])  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=20, blank=True, null=True, choices=[("Teacher", "Teacher"), ("Accountant", "Accountant"), ("Receptionist", "Receptionist"), ("Other", "Other")])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'