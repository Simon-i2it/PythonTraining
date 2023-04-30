from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("reviews", views.ReviewsView.as_view()),
    path("review/<int:pk>", views.ReviewDetailView.as_view(), name="url-review-detail"),
    path(
        "thank_you/<str:username>", views.ThankYouView.as_view(), name="url-thank-you"
    ),
]
