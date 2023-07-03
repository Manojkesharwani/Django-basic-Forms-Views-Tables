from .models import project
# from . import forms
from django import forms

class myform(forms.ModelForm):
    class Meta:
        model = project
        fields='__all__'

