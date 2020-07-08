from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import User,Profile
from django.contrib.auth.models import Group 

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender=User)
def set_user_group(sender,instance,created,**kwargs):
    if created:
        user_group = Group.objects.get(name = "User")
        instance.groups.add(user_group)

