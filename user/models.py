from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model) :
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	balance = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user.username} Profile'
