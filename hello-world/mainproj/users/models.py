from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.

# first option
from django.db.models.signals import post_save, post_delete
# second option (alternative)
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True,
        upload_to='profiles/', default='profiles/default.jpg')
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def profileUpdate(sender, instance, created, **kwarg):
    print('Profile Saved!')
    if created:
        profile = Profile.objects.create(
            user = instance,
            name = instance.username
        )

@receiver(post_delete, sender=User)
def profileDelete(sender, instance, **kwarg):
    print('Deleting Profile!')

# first option
#post_save.connect(profileUpdate, sender=Profile)
#post_delete.connect(profileDelete, sender=Profile)
# second option is: using "@receiver" decorator ...
