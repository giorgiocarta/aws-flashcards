from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    category = models.CharField(max_length=300)

    # date_posted = models.DateTimeField(default=timezone.now)
    # last_modified = models.DateTimeField(auto_now=True)
    # do we want to delete the post when the user is deleted?
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}...".format(self.category.upper(), self.question[0:100])