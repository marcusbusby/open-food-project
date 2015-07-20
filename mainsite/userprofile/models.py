from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	contributor = models.BooleanField(default=False)
	address = models.CharField(max_length=100, default='')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


# Create your models here.
