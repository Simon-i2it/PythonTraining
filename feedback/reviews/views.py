from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request: HttpRequest):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request: HttpRequest):
        form = ReviewForm(request.POST)
        # form = ReviewForm(request.POST, Review.objects.get(username="username")) # to update record
        if form.is_valid():
            form.save()
            return redirect("url-thank-you", form.cleaned_data["username"])


class ThankYouView(View):
    def get(self, request: HttpRequest, username: str):
        return render(request, "reviews/thank_you.html", {"username": username})
