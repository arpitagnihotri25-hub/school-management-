from django import forms
from classteacher.models import Classteacher
    
class ClassteacherForm(forms.ModelForm):
    class Meta:
        model=Classteacher
        fields=['class_number','section','class_teacher_name','staff_id']

        labels={'class_number':'Class',
                'section':'Section',
                'class_teacher_name':'Class Teacher Name',
                'staff_id':'Staff ID'}
        
        widgets={'class_number':forms.Select(attrs={'placeholder':"Select Class",'id':"classField",'name':"class"}),
                'section':forms.Select(attrs={'placeholder':"Select Section",'id':"section",'name':"section"}),
                'class_teacher_name':forms.TextInput(attrs={'placeholder':"Enter Class Teacher Name",'id':"fullName"}),
                'staff_id':forms.TextInput(attrs={'placeholder':"Enter the Staff ID", 'id':"staffId"})}