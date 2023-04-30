from django.http import HttpRequest
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def review(request: HttpRequest):
    form = ReviewForm()
    if request.method == "POST":
        username = form.cleaned_data["username"]
        instance = Review.objects.get(username=username)

        if instance is not None:
            form = ReviewForm(request.POST, instance=instance)
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(
                thank_you,
            )
    return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
