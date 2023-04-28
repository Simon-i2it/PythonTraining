from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} [{self.published_date.strftime('%Y')}] ({self.rating}*)"
