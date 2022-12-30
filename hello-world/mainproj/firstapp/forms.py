from django.forms import ModelForm
from .models import FirstApp

class ProjectForm(ModelForm):
    class Meta:
        model = FirstApp
        # fields = '__all__'
        fields = ['title', 'tags'] 