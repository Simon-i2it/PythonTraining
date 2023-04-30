from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(TemplateView):
    def get(self, request: HttpRequest):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request: HttpRequest):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("url-thank-you", form.cleaned_data["username"])


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
