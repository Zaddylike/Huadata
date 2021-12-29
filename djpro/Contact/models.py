from django.db import models

import django.utils.timezone as timezone

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=20, null = False, blank = False)
    name = models.CharField(max_length = 10, null = False, blank = False)
    email = models.EmailField(max_length=20, null = False, blank = False)
    comment = models.TextField(max_length= 300, null = False, blank = False)
    create_time = models.DateTimeField("createtime",default = timezone.now)
    # update_time = models.DateTimeField('updatetime', auto_now=True)

    def __str__(self): #call func return curusr-name
        return self.name


