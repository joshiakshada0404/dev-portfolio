from django.forms import ModelForm
from .models import Project

class projectForm(ModelForm):

    class Meta :
        model = Project
        fields = ['title','thumbnail','body']


def __init__(self,*args, **kwargs):
    super(projectForm,self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update(
        {'class': 'form-control'})
    self.fields['body'].widget.attrs.update(
        {'class':'form-control', } )
        
    
        