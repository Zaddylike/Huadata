from django import forms
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject','name','email','comment') #limit display field 
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'})
        }

