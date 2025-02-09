from django import forms
from .models import OS, OSProduto
from django.forms import inlineformset_factory

class OSForm(forms.ModelForm):
    class Meta:
        model = OS
        fields = '__all__'


class OSProdutoForm(forms.ModelForm):
    class Meta:
        model = OSProduto
        fields = ['produto', 'quantidade']


OSProdutoForm = inlineformset_factory(OS, OSProduto, form=OSProdutoForm, extra=1)
