from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField(default='this is cool')
    desription = models.TextField()
    data = models.TextField()
