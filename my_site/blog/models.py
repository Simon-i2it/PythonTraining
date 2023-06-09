from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    image = models.CharField(max_length=254)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"[{self.title}] by {self.author.first_name} {self.author.last_name} on {self.date}"

    def get_absolute_url(self):
        return reverse("url_post", args=[self.slug])
