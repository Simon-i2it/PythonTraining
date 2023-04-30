from django.db import models

# Create your models here.


class Profile(models.Model):
    image_file = models.FileField(upload_to="images")
