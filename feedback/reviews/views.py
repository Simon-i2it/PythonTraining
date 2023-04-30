from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"

    def get_success_url(self) -> str:
        return reverse("url-thank-you", args=[self.request.POST.get("username")])


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewsView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "reviews/reviews.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(rating__gte=2)


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"
