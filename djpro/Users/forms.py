from django import forms
from django.contrib.auth.models import User
import re

def check_email(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern,email)

class RegistraionForm(forms.Form):
    
    username = forms.CharField(label='username',max_length=50)
    email = forms.EmailField(label='Email',)
    password = forms.CharField(label='Passwrod', widget=forms.PasswordInput)
    pasconfirm = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    #Use clean methods to define custom validation rules
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) <6:
            raise forms.ValidationError('Your username nust beat least 6 characters long')
        elif len(username)>50:
            raise forms.ValidationError('Your username is too long')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) >0:
                raise forms.ValidationError('Your username already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if check_email(email):
            filter_result = User.objects.filter(email__exact = email)
            if len(filter_result) >0:
                raise forms.ValidationError('Your email already exists')
        else:
            raise forms.ValidationError('Please enter a valid email')
        
        return email

    def clena_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(password) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password
    
    def clean_pascomfirm(self):

        
        password = self.cleaned_data.get('password')
        pasconfirm = self.cleaned_data.get('passconfirm')
        
        if password and pasconfirm and password != pasconfirm :
            raise forms.ValidationError('Password mismatch. Please enter again')
        
        return pasconfirm

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=50)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    #Use clean method to define custom validation rules

    def clean_username(self):

        username = self.cleaned_data.get('username')
        

        if check_email(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError("This email does not exist.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError("This username does not exist. Please register first.")

        return username

class ProfileForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    name = forms.CharField(label='Nike Name',max_length=50, required=False)

class PaschangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput)

    new_password = forms.CharField(label='New Password',widget=forms.PasswordInput)
    check_newpassword = forms.CharField(label='New Password Confirmation',widget=forms.PasswordInput)

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')

        if len(new_password) <6:
            raise forms.ValidationError('Your password is too short')
        elif len(new_password) >20:
            raise forms.ValidationError('Your password is too long')
        
        return new_password
    def clean_check_newpassword(self):
        new_password = self.cleaned_data.get('new_password')
        check_newpassword = self.cleaned_data.get('check_newpassword')

        if new_password and check_newpassword and new_password != check_newpassword:
            raise forms.ValidationError("Password mismatch. Please enter again")
        
        return check_newpassword
