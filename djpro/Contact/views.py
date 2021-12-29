from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import ContactModelForm

# Create your views here.


def ContactView(request):
    forms = ContactModelForm()
    
    if request.method == 'POST':
        forms = ContactModelForm(data = request.POST)
        if forms.is_valid():
            # forms.save()
            messages.success(request, 'Message sent !')
            # return redirect('/About/Contact')
    context = {
        'form':forms
    }
    return render(request, 'about-contact.html', context)