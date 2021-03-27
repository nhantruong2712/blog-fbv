from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=32, blank=True)
	last_name = models.CharField(max_length=32, blank=True)
	email = models.EmailField(max_length=100)
	bio = models.TextField(blank=True)
	signup_confirmation = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
# With the @receiver decorator, we can link a signal with a function.
# So, every time that a User model instance ends to run its save() method (or when user register ends),
# the update_profile_signal will start to work right after user saved.
def update_profile_signal(sender, instance, created, **kwargs):
	# sender - The model class.
	# instance - The actual instance being saved.
	# created - A boolean; True if a new record was created.
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
