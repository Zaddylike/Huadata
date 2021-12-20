from django.shortcuts import render

# Create your views here.
from .models import Home


def homeView(request):
    return render(request,'home.html')    
