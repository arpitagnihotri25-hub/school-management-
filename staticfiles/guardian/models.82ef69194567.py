from django.db import models
from student.models import Student
from django.contrib.auth.models import User

class Guardian(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, blank=True, null=True, related_name="guardian")
    guardian_id = models.CharField(db_column='Guardian_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.BigIntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    admission_no = models.ForeignKey(Student, models.DO_NOTHING, db_column='admission_no', blank=True, null=True)
    occupation = models.CharField(db_column='Occupation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=10, blank=True, null=True, choices=[("Mother", "Mother"), ("Father", "Father")])  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guardian'