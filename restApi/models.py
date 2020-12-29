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

@receiver(post_delete, sender=MyModel)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False) 
    
class File(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    module = models.CharField(max_length=500,blank=False, null=True)
    type = models.CharField(max_length=50)
    file = models.FileField(blank=False, null=False, upload_to='media/')
    def __str__(self):
        return self.file.name        
    def delete(self, using=None, keep_parents=False):
        self.song.storage.delete(self.song.name)
        self.image.storage.delete(self.song.name)
        super().delete()

class Post(models.Model):
    title = models.CharField(max_length=300,blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    content = models.TextField(blank=False, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    side_nav = models.BooleanField(blank=True, null=True)
    def __str__(self):
        return self.title       

# class ManagementHistory(models.Model):
#     date = models.CharField(max_length=100,blank=False, null=True)
#     person = models.CharField(max_length=100,blank=False, null=True)
#     type = models.CharField(max_length=100,blank=False, null=True)
#     def __str__(self):
#         return self.title       

# class ImoprtantEvent(models.Model):
#     date = models.CharField(max_length=100,blank=False, null=True)
#     event = models.CharField(max_length=500,blank=False, null=True)
#     def __str__(self):
#         return self.title       

