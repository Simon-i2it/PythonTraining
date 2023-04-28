from django.urls import path
from . import views

urlpatterns = [
    # path('insert_books', views.insert_books),
    path("index", views.index, name="url_index")
]
