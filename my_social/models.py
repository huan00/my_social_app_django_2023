from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.
# class Image(models.Model):
#     image = models.ImageField(upload_to='media/')

#     def __str__(self):
#         return str(datetime.date.today())

class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    friends = ArrayField(models.CharField(max_length=100), blank=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', default='')
    location = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    viewedProfile = models.IntegerField(default=0, blank=True)
    impressions = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.id)


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userId')
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='media/', default='')
    likes = models.JSONField(default=dict, blank=True)
    comments = ArrayField(models.TextField(), blank=True)

    def __str__(self):
        return str(self.id)


