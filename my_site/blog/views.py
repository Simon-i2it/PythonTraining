from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

dict_posts = [
    {
        "slug": "digital-art",
        "title": "Digital Art",
        "image": "digital-art.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 26),
        "summary": """
            Artists and designers can enhance their digital artwork with a pen drawing tablet.
            This device enables the use of a stylus, providing more control and precision in digital art creation.
        """,
        "content": """
            - Flexibility: Easily make changes, experiment with techniques, colors, and compositions without starting over. 
            - Access to tools: Wide range of tools and features, including layers, brushes, filters, and effects. 
            - Environmentally friendly: No need for paper, paint, or other traditional art supplies.
        """,
    },
    {
        "slug": "table-tennis",
        "title": "Table Tennis",
        "image": "table-tennis.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 27),
        "summary": """
            Table tennis aka ping pong, is the most popular racket sport in the world, with over 300 million active players
            and was played in England in the 1880s instead of tennis and was included in the Olympic Games in 1988.
        """,
        "content": """
            - Improves hand-eye coordination and reflexes.
            - Increases physical activity, burning calories and improving cardiovascular health.
            - Promotes socialization and allows individuals to meet new people.
            - Reduces stress and provides an enjoyable way to relieve tension.
            - Enhances mental acuity, requiring strategic thinking, concentration, and focus.
            - Improves balance and coordination through quick movements and changes in direction.
        """,
    },
]


def welcome(request: HttpRequest) -> HttpResponse:
    latest_posts = dict_posts[-2:]
    return render(request, "blog/welcome.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/posts.html", {"posts": dict_posts})


def post(request: HttpRequest, slug) -> HttpResponse:
    correct_post = next(post for post in dict_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": correct_post})
