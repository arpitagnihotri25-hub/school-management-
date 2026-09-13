from django import forms
from student.models import Student
    
class register_student(forms.ModelForm):
    
    class Meta:
        model=Student
        fields=['name','class_field','section','father_name','mother_name','father_occupation','mother_occupation','father_contact','mother_contact','dob','address','gender','house','blood_group','mode_of_transport']

        labels={'name':'Student Name',
                'class_field':'Class',
                'section':'Section',
                'father_name':"Father's Name",
                'mother_name':"Mother's Name",
                'father_occupation':"Father's Occupation",
                'mother_occupation':"Mother's Occupation",
                'father_contact':"Father's Contact",
                'mother_contact':"Mother's Contact",
                'dob':'Date of Birth',
                'address':'Address',
                'gender':'Gender',
                'house':'House',
                'blood_group':'Blood Group',
                'mode_of_transport':'Mode of Transport'}

        widgets={'name':forms.TextInput(attrs={'placeholder':"Enter Student's Full Name",'id':"fullName"}),
                'class_field':forms.Select(attrs={'placeholder':"Select Class",'id':"classField"}),
                'section':forms.Select(attrs={'placeholder':"Select Section",'id':"section"}),
                'father_name':forms.TextInput(attrs={'placeholder':"Enter Student's Father Name",'id':"father_name"}),
                'mother_name':forms.TextInput(attrs={'placeholder':"Enter Student's Mother Name",'id':"mother_name"}),
                'father_contact':forms.NumberInput(attrs={'placeholder':"Enter Father's Contact Number",'id':"father_contact"}),
                'mother_contact':forms.NumberInput(attrs={'placeholder':"Enter Mother's Contact Number",'id':"mother_contact"}),
                'father_occupation':forms.TextInput(attrs={'placeholder':"Enter Father's Occupation",'id':"father_occupation"}),
                'mother_occupation':forms.TextInput(attrs={'placeholder':"Enter Mother's Occupation",'id':"mother_occupation"}),
                'dob':forms.DateInput(attrs={'placeholder':"Enter Date of Birth",'id':"dob",'type':'date'}),
                'address':forms.TextInput(attrs={'placeholder':"Enter Address",'id':"address"}),
                'gender':forms.Select(attrs={'placeholder':"Select Gender",'id':"gender"}),
                'house':forms.Select(attrs={'placeholder':"Select House",'id':"house"}),
                'blood_group':forms.Select(attrs={'placeholder':"Select Blood Group",'id':"blood_group"}),
                'mode_of_transport':forms.Select(attrs={'placeholder':"Select Mode of Transport",'id':"mode_of_transport"}),}