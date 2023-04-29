from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from reviews.forms import ReviewForm

# Create your views here.


def review(request: HttpRequest):
    form: ReviewForm = ReviewForm()
    if request.method == "POST":
        submitted_form = ReviewForm(request.POST)
        if submitted_form.is_valid():
            return redirect(thank_you, submitted_form.cleaned_data["username"])
    else:
        return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
