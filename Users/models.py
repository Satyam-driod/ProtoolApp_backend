from django.db import models
from django.conf import settings
from django.db.models.signals import post_save 
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Work (models.Model):

    title = models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=False)

    def __str__(self):
        return self.title
        