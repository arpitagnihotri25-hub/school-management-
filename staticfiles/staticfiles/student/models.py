from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    admission_no = models.CharField(db_column='Admission_No', max_length=20, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True, choices=[("Class 9th", "Class 9th"), ("Class 10th", "Class 10th"), ("Class 11th", "Class 11th"), ("Class 12th", "Class 12th")])
    section = models.CharField(db_column='Section', max_length=5, blank=True, null=True, choices=[("A", "A"), ("B", "B"), ("C", "C")])  # Field name made lowercase.
    father_name = models.CharField(db_column='Father_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mother_name = models.CharField(db_column='Mother_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    father_occupation = models.CharField(db_column='Father_Occupation', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mother_occupation = models.CharField(db_column='Mother_Occupation', max_length=25, blank=True, null=True)  # Field name made lowercase.
    father_contact = models.BigIntegerField(db_column='Father_Contact', blank=True, null=True)  # Field name made lowercase.
    mother_contact = models.BigIntegerField(db_column='Mother_Contact', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True,  choices=[("Male", "Male"), ("Female", "Female"), ("Others", "Others")])  # Field name made lowercase.
    house = models.CharField(db_column='House', max_length=10, blank=True, null=True, choices=[("Green", "Green"), ("Blue", "Blue"), ("Red", "Red"), ("Yellow", "Yellow")])  # Field name made lowercase.
    blood_group = models.CharField(db_column='Blood_Group', max_length=5, blank=True, null=True, choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")])  # Field name made lowercase.
    mode_of_transport = models.CharField(db_column='Mode_of_Transport', max_length=20, blank=True, null=True, choices=[("School Bus", "School Bus"), ("Van", "Van"), ("Self", "Self")])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'