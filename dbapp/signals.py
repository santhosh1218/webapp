from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from dbapp.models import Profile

@receiver(post_save,sender=User)
def profile_create(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save,sender=User)
def profile_save(sender,instance,**kwargs):
    instance.profile.save()
