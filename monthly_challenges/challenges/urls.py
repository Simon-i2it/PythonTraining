from . import views
from django.urls import path

urlpatterns = [
    path("", views.challenges, name="challenges"),
    path("<int:month>", views.get_monthly_challenge_int),
    path("<str:month>", views.get_monthly_challenge_str, name="get_monthly_challenge_str"),
]
