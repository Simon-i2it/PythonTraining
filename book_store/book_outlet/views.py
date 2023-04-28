from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from book_outlet.models import Book

# Create your views here.

def insert_books(request:HttpRequest) -> HttpResponse:

    books = [
        Book(title="Harry Potter - The Philosopher's Stone", rating=8, published_date="1997-06-26"),
        Book(title="Harry Potter - The Chamber of Secrets", rating=7, published_date="1998-07-02"),
        Book(title="Harry Potter - The Prisoner of Azkaban", rating=4, published_date="1999-07-08"),
        Book(title="Harry Potter - The Goblet of Fire", rating=5, published_date="2000-07-08"),
        Book(title="Harry Potter - The Order of Phoenix", rating=4, published_date="2003-06-21"),
        Book(title="Harry Potter - The Half-Blood Prince", rating=9, published_date="2005-07-16"),
        Book(title="Harry Potter - The Deathly Hallows", rating=8, published_date="2007-07-21"),
        Book(title="The Hunger Games", rating=9, published_date="2008-09-14"),
        Book(title="Catching Fire", rating=8, published_date="2009-09-01"),
        Book(title="Mockingjay", rating=7, published_date="2010-08-24"),
    ]

    for book in books:
        book.save()

    return HttpResponse(Book.objects.all())

def get_books(request:HttpRequest) -> HttpResponse:

    return HttpResponse(Book.objects.all())
    