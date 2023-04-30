from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView


from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank_you"

    def get_success_url(self) -> str:
        return f"{super().get_success_url()}/{self.request.POST.get('username')}"

    def form_valid(self, form: ReviewForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewsView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "reviews/reviews.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(rating__lte=2)


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"
