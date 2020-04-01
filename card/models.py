from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return "{}-{}".format(self.pk, self.name)


class Card(models.Model):
	question = models.CharField(max_length=100)
	answer = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return "{}-{}...".format(self.pk, self.question[0:100])
