from django.db import models

# Create your models here.


class Post(models.Model):
    # title = models.CharField(max_length=120)
    desription = models.TextField(blank=True, null=True)
    number = models.DecimalField(max_digits=1000, decimal_places=2)
    comment = models.TextField()
