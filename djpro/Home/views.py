from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# Create your views here.
from .models import Home


def homeView(request):
    return render(request,'home.html',)    
