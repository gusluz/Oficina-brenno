from django import forms
from .models import OS

class OSForm(forms.ModelForm):
    class Meta:
        model = OS
        fields = '__all__'