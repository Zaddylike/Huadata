from django.db import models
from datetime import date
from django.urls import reverse
import os
from uuid import uuid4
# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'album'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Picture(models.Model):
    title = models.CharField('Title', max_length=100, blank=True, default='')
    image = models.ImageField('Picture', upload_to=path_and_rename,blank=True)
    user = models.CharField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pic_upload:pic_detail',args=[str(self.id)])
