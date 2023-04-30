from django.http import HttpRequest
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def review(request: HttpRequest):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # form = ReviewForm(request.POST, Review.objects.get(username="username")) # to update record

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return redirect(thank_you, username)

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
