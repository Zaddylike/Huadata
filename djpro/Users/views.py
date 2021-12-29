from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from django.contrib.auth.models import User
from .models import Users_models

from .forms import ProfileForm, RegistraionForm, LoginForm, PaschangeForm

# Create your views here.
def register(request):
    form = RegistraionForm()
    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pasconfirm']

            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            userProfile = Users_models(user=user)
            userProfile.save()
            return HttpResponseRedirect('thejuicy/')

    context = {
        'form' : form
    }
    return render(request,'registration.html',context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            curusr = auth.authenticate(username=username, password=password)

            if curusr is not None and curusr.is_active:
                auth.login(request,curusr)
                return HttpResponseRedirect(reverse('Users:profile', args=[curusr.id]))
            else:
                return render(request, 'login.html', {'form': form,'message': 'Wrong password. Please try again.'})
    context = {
        'form':form
    }
    r=User.objects.filter(password='efai2021')
    print(r)
    return render(request,'login.html',context)

def logout(request):

    auth.logout(request)

    return HttpResponseRedirect('/users/login/')

@login_required
def profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    context ={
        'user':user
    }
    return render(request, 'profile.html', context)

@login_required
def paschange(request,pk):
    user = get_object_or_404(User,pk=pk)
    form = PaschangeForm()
    if request.method == "POST":

        form = PaschangeForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data['old_password']
            username = user.username
            
            user = auth.authenticate(username=username,password=password)

            if user is not None and user.is_active:
                new_password = form.cleaned_data['check_newpassword']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect('/users/login/')
    context ={
        'form':form,
        'user':user,
        'message': 'Old password is wrong. Try again'
    }
    return render(request, 'paschange.html', context)

@login_required
def profile_update(request,pk):
    user = get_object_or_404(User,pk=pk)
    user_profile = get_object_or_404(Users_models,user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user_profile.name = form.cleaned_data['name']
            user_profile.save()

            return HttpResponseRedirect(reverse('Users:profile',args=[user.id]))
    default_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'name': user_profile.name,
        }
    context ={
        'user':user,
        'form' : ProfileForm(default_data)
    }

    return render(request, 'profile_update.html', context)
