from django.db import models

import django.utils.timezone as timezone
from django.contrib.auth.models import User
# Create your models here.
class Users_models(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='name')

    create_date = models.DateTimeField(default=timezone.now, verbose_name='save_date')
    update_date = models.DateTimeField(auto_now=True,verbose_name='update_date')

    def __str__(self):
        return self.user
