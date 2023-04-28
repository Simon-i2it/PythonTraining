from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(null=True, max_length=50)
    published_date = models.DateField()
    is_best_seller = models.BooleanField(default=False)
    rating = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )

    def __str__(self):
        return f"{self.title} [{self.published_date.strftime('%Y')}] ({self.rating}*)"
