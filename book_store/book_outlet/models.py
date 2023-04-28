from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(blank=True, editable=False, null=False, db_index=True)

    def __str__(self):
        return f"{self.title} [{self.published_date.strftime('%Y')}] by {self.author} (Rating: {self.rating})"

    def get_absolute_url(self):
        return reverse(viewname="url_book_int", args=[self.pk])

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
