from django.db import models

class Classteacher(models.Model):
    class_number = models.CharField(db_column='Class_Number',max_length=10, blank=True, null=True, choices=[("Class 9th", "Class 9th"), ("Class 10th", "Class 10th"), ("Class 11th", "Class 11th"), ("Class 12th", "Class 12th")])  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=5, blank=True, null=True,choices=[("A", "A"), ("B", "B"), ("C", "C")])  # Field name made lowercase.
    class_teacher_name = models.CharField(db_column='Class_teacher_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staff_id = models.CharField(db_column='Staff_ID', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classteacher'