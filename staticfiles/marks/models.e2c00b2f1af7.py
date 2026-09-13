from django.db import models

class Marks(models.Model):
    marks_id = models.IntegerField(primary_key=True)
    admission_no = models.ForeignKey('student.Student', models.DO_NOTHING, db_column='Admission_No', blank=True, null=True)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    section = models.CharField(db_column='Section', max_length=20, blank=True, null=True)  # Field name made lowercase.
    marks_obt = models.DecimalField(db_column='Marks_obt', max_digits=5, decimal_places=2, blank=True, null=True) 
    total_marks = models.DecimalField(db_column='total_Marks', max_digits=5, decimal_places=2, blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marks'