from django.urls import path

from . import views

urlpatterns = [
    path("create", views.ProfileView.as_view(), name="url-profile"),
]
