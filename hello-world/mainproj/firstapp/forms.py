from django.forms import ModelForm, widgets
from django import forms
from .models import FirstApp

class ProjectForm(ModelForm):
    class Meta:
        model = FirstApp
        # fields = '__all__'
        fields = ['title', 'tags', 'img'] 
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-custom-class'})

        # self.fields['title'].widget.attrs.update({'class': 'my-custom-class', 'placeholder': 'add title'})
