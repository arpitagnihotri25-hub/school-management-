from django import forms
from guardian.models import Guardian
    
class register_guardian(forms.ModelForm):
    
    class Meta:
        model=Guardian
        fields=['admission_no','name','contact','email','relation','occupation','address']

        labels={'admission_no':"Student's Admission Number",
                'name':'Full Name',
                'contact':'Contact Number',
                'email':'Email',
                'relation':'Relation with Student',
                'occupation':'Occupation',
                'address':'Address',}
        
        widgets={'admission_no':forms.TextInput(attrs={'placeholder':"Enter Student's Admission Number",'id':"admission_number"}),
                'name':forms.TextInput(attrs={'placeholder':"Enter Your Full Name",'id':"fullName"}),
                'email':forms.EmailInput(attrs={'placeholder':"Enter Your Email ID",'id':"email"}),
                'contact':forms.NumberInput(attrs={'placeholder':"Enter Your Contact Number",'id':"contact"}),
                'relation':forms.Select(attrs={'placeholder':"Enter Your relationship with student",'id':"relation"}),
                'occupation':forms.TextInput(attrs={'placeholder':"Enter Your Occupation",'id':"occupation"}),
                'address':forms.TextInput(attrs={'placeholder':"Enter Your Address",'id':"address"})}