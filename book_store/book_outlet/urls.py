from . import views
from django.urls import include, path

urlpatterns = [
    path('insert', views.insert_books),
    path('print', views.print_books)
]