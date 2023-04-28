from django.urls import path
from . import views

urlpatterns = [
    path("insert_books", views.insert_books),
    path("save_books", views.save_books),
    path("books", views.books, name="url_books"),
    path("book/<int:id>", views.book_int, name="url_book_int"),
    path("book/<slug:slug>", views.book_slug, name="url_book_slug"),
]
