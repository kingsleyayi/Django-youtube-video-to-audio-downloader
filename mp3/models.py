from django.db import models

# Create your models here.
class Song(models.Model):
	name = models.CharField(max_length=200, null=True)
	year = models.CharField(max_length=200, null=True)
	artist =models.CharField(max_length=200, null=True)
	audio = models.FileField(null =True, blank=True)

	def __str__(self):
		return self.name

class Messages(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=200, null=True)
	message =models.CharField(max_length=400, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
