from django import forms
from . models import Employe

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employe
        fields='__all__'

        widgets={
            'Password':forms.PasswordInput(),
        }

