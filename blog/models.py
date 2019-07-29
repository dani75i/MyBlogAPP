from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.username


class AllPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):

        return self.title