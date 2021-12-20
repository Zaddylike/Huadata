from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__" #limit display field 
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'})
        }

class LoginForm(forms.Form):
    account = forms.CharField(
        label="Account",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        }