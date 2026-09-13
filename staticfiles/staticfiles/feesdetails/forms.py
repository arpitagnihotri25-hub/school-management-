from django import forms
from feesdetails.models import FeeDetails
    
class fees__details(forms.ModelForm):
    class Meta:
        model=FeeDetails
        fields=['class_field','amount']

        labels={'class_field':'Class',
                'amount':'Fees Amount'}
        
        widgets={'class_field':forms.Select(attrs={'placeholder':"Select Class",'id':"classField",'class':'fee-input'}),
                'amount':forms.NumberInput(attrs={'placeholder':"Enter the Fees Amount",'id':"feesAmount",'class':'fee-input'})}