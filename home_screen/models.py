from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Transfer(models.Model) :
	amount = models.IntegerField(default=0)
	date_transferred = models.DateTimeField(default = timezone.now)
	sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
	receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')



