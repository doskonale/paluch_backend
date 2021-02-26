from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class File(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    module = models.CharField(max_length=500,blank=False, null=True)
    type = models.CharField(max_length=50)
    file = models.FileField(blank=False, null=False, upload_to='media/')
    def __str__(self):
        return self.file.name        

@receiver(post_delete, sender=File)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False) 


class Post(models.Model):
    title = models.CharField(max_length=300,blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    content = models.TextField(blank=False, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    side_nav = models.BooleanField(blank=True, null=True)
    def __str__(self):
        return self.title       


class GardenInfo(models.Model):
    name = models.CharField(max_length=100,blank=False, null=True)
    value = models.CharField(max_length=100,blank=False, null=True)
    type = models.CharField(max_length=100,blank=False, null=True)
    def __str__(self):
        return self.name       


class GardenHistory(models.Model):
    column1 = models.CharField(max_length=100,blank=False, null=True)
    column2 = models.CharField(max_length=500,blank=False, null=True)
    column3 = models.CharField(max_length=100,blank=False, null=True)
    def __str__(self):
        return self.name       
