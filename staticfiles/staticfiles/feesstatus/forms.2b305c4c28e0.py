from django import forms
from feesstatus.models import FeesStatus
    
class fees__status(forms.ModelForm):
    class Meta:
        model=FeesStatus
        fields=['status_id','admission_no','student_name','class_field','section','deposit_date','deposit_amount']

        labels={'admission_no':'Admission Number',
                'student_name':'Student Name',
                'class_field':'Class',
                'section':'Section',
                'deposit_date':'Deposit Date',
                'deposit_amount':'Deposit Amount'}
        
        widgets={'admission_no':forms.TextInput(attrs={'placeholder':"Enter the Admission Number", 'id':"admissionNo"}),
                'student_name':forms.TextInput(attrs={'placeholder':"Enter Your Full Name",'id':"fullName"}),
                'class_field':forms.Select(attrs={'placeholder':"Select Class",'id':"classField"}),
                'section':forms.Select(attrs={'placeholder':"Select Section",'id':"section"}),
                'deposit_date':forms.DateInput(attrs={'placeholder':"Enter the Deposit Date",'id':"depositDate"}),
                'deposit_amount':forms.NumberInput(attrs={'placeholder':"Enter the Deposit Amount",'id':"depositAmount"})}