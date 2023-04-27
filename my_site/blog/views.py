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
        "date": date(2023, 4, 25),
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
        "date": date(2023, 4, 26),
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
    {
        "slug": "cycling",
        "title": "Cycling",
        "image": "cycling.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 27),
        "summary": """
            Are you looking to stay healthy while also making a positive impact on the environment? 
            Look no further than cycling ! As a cyclist, improve your own health & fitness, 
            and also combat climate change by reducing traffic congestion.
        """,
        "content": """
            - Enhanced cardiovascular health : regular cycling can help to lower blood pressure, reduce the risk of heart disease, and improve overall heart health.
            - Reduced stress and anxiety : cycling provides a sense of freedom and escape from daily stressors, allowing you to clear your mind and enjoy the outdoors.
            - Improved overall fitness and endurance : cycling is an excellent form of exercise that engages multiple muscle groups and can help you build endurance and strength over time.
            - Lower risk of chronic diseases : cycling has been shown to lower the risk of chronic diseases such as diabetes, obesity, and heart disease.
            - Enhanced mental wellbeing : cycling can help boost your mood and improve mental health, reducing symptoms of anxiety and depression.
            - Improved joint mobility and flexibility : cycling is a low-impact form of exercise that can help increase joint mobility and flexibility.
            - Reduced impact on the environment : cycling is an environmentally friendly mode of transportation that produces no carbon emissions and helps reduce traffic congestion.
            - Increased social connections : cycling provides a great opportunity to connect with like-minded individuals, whether through group rides, clubs, or races.
            - Improved sleep quality : cycling can help regulate your sleep cycle, leading to better quality sleep and more restful nights.
            - Cost-effective : cycling is a relatively low-cost activity that requires minimal equipment, making it accessible to a wide range of people.
        """,
    },
    {
        "slug": "photography",
        "title": "Photography",
        "image": "photography.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 28),
        "summary": """
            Are you interested in capturing the beauty of the world around you?
            Look no further than photography! As a photographer, you can explore your creativity and express yourself while capturing moments and memories.
        """,
        "content": """
            - Express creativity : photography allows you to express your creativity and capture unique and beautiful images that showcase your perspective.
            - Preserve memories : photography is a great way to capture special moments and memories, preserving them for a lifetime.
            - Develop patience and attention to detail : photography requires patience and attention to detail in order to capture the perfect shot.
            - Learn about the world : photography can be a tool for exploring and learning about the world around you, including nature, cultures, and people.
            - Improve technical skills : photography involves learning technical skills such as lighting, composition, and editing, which can improve your overall photography ability.
            - Develop a unique style : through experimentation and practice, photographers can develop a unique style that sets them apart from others.
            - Connect with others : photography can be a great way to connect with others who share your passion, whether through online communities or in-person events.
            - Boost confidence : successfully capturing a great shot can be a confidence booster, improving your self-esteem and sense of accomplishment.
            - Tell a story : photography can tell a story through a single image, conveying emotions and experiences in a powerful way.
            - Find beauty in everyday life : photography encourages you to look for the beauty in everyday life, finding inspiration in the world around you.
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
