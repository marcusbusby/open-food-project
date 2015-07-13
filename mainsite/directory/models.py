from django.db import models
from django.utils import timezone

class Food(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	base_amount = models.IntegerField()
	base_unit = models.CharField(max_length = 10)



# Create your models here.
