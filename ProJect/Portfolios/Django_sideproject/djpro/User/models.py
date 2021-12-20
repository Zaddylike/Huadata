from django.db import models

import django.utils.timezone as timezone
# Create your models here.

class User(models.Model):
    account= models.CharField(max_length=20, null = False, blank = False, unique=True)
    password= models.CharField(max_length=20, null = False, blank = False)
    email= models.EmailField(max_length=40, null = False)
    name=models.CharField(max_length=10, null = False, blank = False)
    create_time = models.DateTimeField("createtime",default = timezone.now)
    update_time = models.DateTimeField('updatetime', auto_now=True)
    def __str__(self):
        return self.name