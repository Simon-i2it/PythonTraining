from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path(
        "thank_you/<str:username>", views.ThankYouView.as_view(), name="url-thank-you"
    ),
]
