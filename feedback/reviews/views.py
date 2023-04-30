from typing import Any, Dict
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from reviews.forms import ReviewForm

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
