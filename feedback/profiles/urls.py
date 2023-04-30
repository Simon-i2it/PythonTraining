from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProfileView.as_view(), name="url-profile"),
    path("all", views.ProfilesView.as_view(), name="url-profiles"),
]
