from . import views
from django.urls import path

urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    path("<int:month>", views.get_challenge_by_month_number),
    path("<str:month>", views.get_challenge),
]
