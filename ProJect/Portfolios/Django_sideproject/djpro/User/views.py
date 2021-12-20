from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import RegisterForm,LoginForm
from .models import User

def signupView(request):

    form = RegisterForm()

    if request.method =='POST':
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'signup.html', context)

def loginView(request):

    form = LoginForm()
    if request.method == 'POST':
        account = request.POST.get("account")
        password = request.POST.get("password")
        
        form = LoginForm(request.POST)
        if form.is_valid:
            curusr=User.objects.filter(account__contains=account).first()
            user = authenticate(User,username=account,password=password)
            
        if user is not None:
            
            login(request,user)
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request,'login.html',context)

def logoutView(request):
    logout(request)

    return redirect('/')