from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['state', 'type_of', 'reference_number', 'd_type']