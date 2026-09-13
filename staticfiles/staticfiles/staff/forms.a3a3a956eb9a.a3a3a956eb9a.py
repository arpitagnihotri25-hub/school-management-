from django import forms
from staff.models import Staff
    
class register_staff(forms.ModelForm):
    
    class Meta:
        model=Staff
        fields=['name','email','contact','qualifications','experience','subject','class_field','address','gender','role']

        labels={'name':'Full Name',
                'email':'Email',
                'contact':'Contact Number',
                'qualifications':'Qualification',
                'experience':'Experience',
                'subject':'Subject',
                'class_field':'Class',
                'address':'Address',
                'gender':'Gender',
                'role':'Role'}
        
        widgets={'name':forms.TextInput(attrs={'placeholder':"Enter Your Full Name",'id':"fullName"}),
                'email':forms.EmailInput(attrs={'placeholder':"Enter Your Email ID",'id':"email"}),
                'contact':forms.NumberInput(attrs={'placeholder':"Enter Your Contact Number",'id':"contact"}),
                'qualifications':forms.TextInput(attrs={'placeholder':"Enter Your Qualification",'id':"qualification"}),
                'experience':forms.TextInput(attrs={'placeholder':"Enter Your Experience",'id':"experience"}),
                'subject':forms.Select(attrs={'placeholder':"Enter the Subject",'id':"subject"}),
                'class_field':forms.Select(attrs={'placeholder':"Select Class",'id':"classField"}),
                'address':forms.TextInput(attrs={'placeholder':"Enter Your Address",'id':"address"}),
                'gender':forms.Select(attrs={'placeholder':"Select Gender",'id':"gender"}),
                'role':forms.Select(attrs={'placeholder':"Select Role",'id':"role"})}