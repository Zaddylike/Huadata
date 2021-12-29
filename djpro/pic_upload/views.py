from typing import List
from django.shortcuts import render

from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from .models import Picture

# Create your views here.

class PicList(ListView):
    queryset = Picture.objects.all().order_by('-date')

    context_object_name = 'latest_picture_list'
    template_name = 'pic_upload/picture_list.html'

class PicDetail(DetailView):
    model = Picture
    template_name = 'pic_upload/picture_detail.html'

class PicUpload(CreateView):
    model = Picture

    fields = ['title','image']

    template_name = 'pic_upload/picture_form.html'