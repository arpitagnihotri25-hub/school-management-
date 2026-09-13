from django.db import models

class FeesStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    admission_no = models.ForeignKey('student.Student', models.DO_NOTHING, db_column='Admission_No', blank=True, null=True)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True, choices=[("Class 9th", "Class 9th"), ("Class 10th", "Class 10th"), ("Class 11th", "Class 11th"), ("Class 12th", "Class 12th")])  # Field name made lowercase. Field renamed because it was a Python reserved word.
    section = models.CharField(db_column='Section', max_length=20, blank=True, null=True, choices=[("A", "A"), ("B", "B"), ("C", "C")])  # Field name made lowercase.
    deposit_date = models.DateField(db_column='Deposit_date', blank=True, null=True)  # Field name made lowercase.
    deposit_amount = models.DecimalField(db_column='Deposit_amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fees_status'