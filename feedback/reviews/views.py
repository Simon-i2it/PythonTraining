from django.http import HttpRequest
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def review(request: HttpRequest):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(form.cleaned_data)
            Review.objects.create(
                username=data["username"],
                feedback=data["feedback"],
                rating=data["rating"],
            )
            return redirect(thank_you, review.username)
    return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
