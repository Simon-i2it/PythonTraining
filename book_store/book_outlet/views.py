from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from book_outlet.models import Author, Book

# Create your views here.


def books(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by("-rating")
    count = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/books.html",
        {"books": books, "count": count, "avg_rating": avg_rating},
    )


def book_int(request: HttpRequest, id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book.html", {"book": book})


def book_slug(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book.html", {"book": book})


def insert_books(request: HttpRequest) -> HttpResponse:
    jk_rowling = Author.objects.get(last_name="Rowling")
    suzanne_collins = Author.objects.get(last_name="Collins")
    chigozie_obioma = Author.objects.get(last_name="Obioma")

    books = [
        Book(
            title="Harry Potter - The Philosopher's Stone",
            published_date="1997-06-26",
            author=jk_rowling,
            is_best_seller=True,
            rating=8,
        ),
        Book(
            title="Harry Potter - The Chamber of Secrets",
            published_date="1998-07-02",
            author=jk_rowling,
            is_best_seller=True,
            rating=7,
        ),
        Book(
            title="Harry Potter - The Prisoner of Azkaban",
            rating=4,
            published_date="1999-07-08",
            author=jk_rowling,
            is_best_seller=True,
        ),
        Book(
            title="Harry Potter - The Goblet of Fire",
            published_date="2000-07-08",
            author=jk_rowling,
            is_best_seller=True,
            rating=5,
        ),
        Book(
            title="Harry Potter - The Order of Phoenix",
            published_date="2003-06-21",
            author=jk_rowling,
            is_best_seller=True,
            rating=4,
        ),
        Book(
            title="Harry Potter - The Half-Blood Prince",
            published_date="2005-07-16",
            author=jk_rowling,
            is_best_seller=True,
            rating=9,
        ),
        Book(
            title="Harry Potter - The Deathly Hallows",
            published_date="2007-07-21",
            author=jk_rowling,
            is_best_seller=True,
            rating=8,
        ),
        Book(
            title="The Hunger Games",
            published_date="2008-09-14",
            author=suzanne_collins,
            rating=9,
        ),
        Book(
            title="Catching Fire",
            published_date="2009-09-01",
            author=suzanne_collins,
            rating=8,
        ),
        Book(
            title="Mockingjay",
            published_date="2010-08-24",
            author=suzanne_collins,
            rating=7,
        ),
        Book(
            title="The Fishermen",
            published_date="2015-04-14",
            author=chigozie_obioma,
            rating=7,
        ),
    ]

    for book in books:
        book.save()

    return HttpResponse(Book.objects.all())


def save_books(request: HttpRequest) -> HttpResponse:
    for book in Book.objects.all():
        book.save()
    return HttpResponse(Book.objects.all())
