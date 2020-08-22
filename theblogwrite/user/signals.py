from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

 

#  this one create a instance user
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

 
#  this one save the created instace user
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
