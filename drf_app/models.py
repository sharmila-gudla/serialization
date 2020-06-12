from django.db import models

from datetime import datetime
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
class Event(models.Model):
    description = models.CharField(max_length=100)
    start = models.DateTimeField()
    finish = models.DateTimeField()
class GameRecord(models.Model):
    score = models.IntegerField()
