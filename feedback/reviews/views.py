from django.http import HttpRequest
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm

# Create your views here.


def review(request: HttpRequest):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            return redirect(thank_you, form.cleaned_data["username"])
    return render(request, "reviews/review.html", {"form": ReviewForm()})


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
