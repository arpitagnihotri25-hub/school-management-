from django import forms
from notice.models import Notice
    
class post_notice(forms.ModelForm):
    class Meta:
        model=Notice
        fields=['notice_id','class_field','title','description','post_date','post_by_name','post_by_id']

        labels={'class_field':'Class',
                'title':'Title',
                'description':'Description',}
        
        widgets={'class_field':forms.TextInput(attrs={'placeholder':"Select Class",'id':"classField"}),
                'title':forms.TextInput(attrs={'placeholder':"Enter the Title", 'id':"title"}),
                'description':forms.Textarea(attrs={'placeholder':"Enter the Description",'id':"description"})}