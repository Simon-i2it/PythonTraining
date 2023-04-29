from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=100)
    feedback = models.TextField(max_length=1000)
    rating = models.IntegerField()
