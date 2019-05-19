from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length=200)

	def Add_To_Cat(self):
		self.save()
		
	def __str__(self):
		return self.cat_name
	