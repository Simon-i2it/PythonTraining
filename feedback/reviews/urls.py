from django.urls import path
from . import views

urlpatterns = [
    path("", views.review),
    path("thank_you/<str:username>", views.thank_you, name="url-thank-you"),
]
