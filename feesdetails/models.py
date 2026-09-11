from django.db import models

class FeeDetails(models.Model):
    class_field = models.CharField(db_column='Class', max_length=15,primary_key=True,choices=[("Class 9th", "Class 9th"), ("Class 10th", "Class 10th"), ("Class 11th", "Class 11th"), ("Class 12th", "Class 12th")])  # Field name made lowercase. Field renamed because it was a Python reserved word.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fee_details'