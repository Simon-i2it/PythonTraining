from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

dict_posts = [
    {
        "slug": "programming",
        "title": "Programming",
        "image": "programming.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 25),
        "summary": """
            Want to expand your skill set and unlock new opportunities in the digital world?
            Look no further than programming! As a programmer, you can develop websites, software, and apps, and bring your ideas to life.
        """,
        "content": """
            - Creative outlet : programming allows you to use your creativity and problem-solving skills to create unique and innovative solutions.
            - High demand : the demand for programmers is constantly increasing, providing job security and opportunities for career growth.
            - Flexibility : programming can be done from anywhere with a computer and internet connection, offering a flexible work schedule and the ability to work remotely.
            - Variety of languages : there are a variety of programming languages to choose from, each with its own strengths and applications, allowing you to find one that fits your interests and goals.
            - Collaboration opportunities : programming often involves working in teams, allowing you to collaborate with others and learn new skills.
            - Continual learning : the constantly evolving nature of technology means that programming requires continual learning and skill development, offering opportunities for personal and professional growth.
            - Improved problem-solving skills : programming requires logical thinking and problem-solving skills, which can be applied to other areas of life.
            - Personal projects : programming allows you to work on personal projects and bring your ideas to life, whether it's a website, app, or software.
            - Increased automation : programming can automate repetitive tasks, saving time and increasing productivity.
            - Impactful solutions : programming has the potential to create impactful solutions to real-world problems, such as improving accessibility, healthcare, and education.
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
        "slug": "photography",
        "title": "Photography",
        "image": "photography.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 27),
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
    {
        "slug": "cycling",
        "title": "Cycling",
        "image": "cycling.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 28),
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
        "slug": "workout",
        "title": "Workout",
        "image": "workout.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 29),
        "summary": """
            Looking to get in shape and improve your overall health?
            Look no further than working out! As a fitness enthusiast, you can improve your physical and mental wellbeing while achieving your fitness goals.
        """,
        "content": """
            - Increased strength and muscle tone : regular workouts can help you build strength and increase muscle tone, leading to improved overall physical fitness.
            - Improved cardiovascular health : workouts such as running, cycling, or swimming can help improve your cardiovascular health, reducing the risk of heart disease and stroke.
            - Reduced stress and anxiety : physical activity can help reduce stress and anxiety by releasing endorphins, improving mood and mental wellbeing.
            - Enhanced flexibility and mobility : incorporating stretching and flexibility exercises into your workouts can help improve joint mobility and overall flexibility.
            - Lower risk of chronic diseases : regular workouts can help reduce the risk of chronic diseases such as diabetes, obesity, and high blood pressure.
            - Improved sleep quality : workouts can help regulate your sleep cycle, leading to better quality sleep and more restful nights.
            - Increased energy levels : physical activity can help increase energy levels, reducing feelings of fatigue and improving overall productivity.
            - Improved mental clarity : regular workouts can improve mental clarity and focus, leading to improved productivity and cognitive function.
            - Enhanced self-esteem : achieving fitness goals and seeing physical improvements can boost self-esteem and confidence.
            - Varied options : there are a wide variety of workouts to choose from, including strength training, cardio, yoga, and more, allowing you to find a workout that fits your preferences and goals.
        """,
    },
    {
        "slug": "digital-art",
        "title": "Digital Art",
        "image": "digital-art.jpg",
        "author": "Simon Alphonse",
        "date": date(2023, 4, 30),
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
]


def welcome(request: HttpRequest) -> HttpResponse:
    latest_posts = dict_posts[-2:]
    return render(request, "blog/welcome.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/posts.html", {"posts": dict_posts})


def post(request: HttpRequest, slug) -> HttpResponse:
    correct_post = next(post for post in dict_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": correct_post})
