from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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


class Post(models.Model):
    title = models.CharField(max_length=300,blank=False, null=True)
    content = models.CharField(max_length=5000,blank=False, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='media/')
    def __str__(self):
        return self.title       