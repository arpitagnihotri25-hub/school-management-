from django.db import models

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    admission_no = models.ForeignKey('student.Student', models.DO_NOTHING, db_column='Admission_No', blank=True, null=True)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_name', max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    section = models.CharField(db_column='Section', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True, choices=[("Present", "Present"), ("Absent", "Absent"), ("Half Day", "Half Day")])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance'
