from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name} [{self.code}]"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    pin_code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.street}, {self.city} - {self.pin_code}, {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    published_date = models.DateField()
    is_best_seller = models.BooleanField(default=False)
    rating = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title} [{self.published_date.strftime('%Y')}] by {self.author} (Rating: {self.rating})"

    def get_absolute_url(self):
        return reverse(viewname="url_book_int", args=[self.pk])

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
