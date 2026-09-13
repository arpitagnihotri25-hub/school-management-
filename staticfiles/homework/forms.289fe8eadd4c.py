from django import forms
from homework.models import Homework
    
class post_homework(forms.ModelForm):
    class Meta:
        model=Homework
        fields=['homework_id','class_field','section','subject','description','post_date','post_by_name','post_by_id']

        labels={'class_field':'Class',
                'section':'Section',
                'description':'Description',}
        
        widgets={'class_field':forms.Select(attrs={'placeholder':"Select Class",'id':"classField"}),
                'section':forms.Select(attrs={'placeholder':"Select Section",'id':"section"}),
                'description':forms.Textarea(attrs={'placeholder':"Enter the Description",'id':"description"})}