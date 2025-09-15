from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "balancing-code-and-music",
        "image": "me-coding.png",
        "author": "Dario",
        "date": date(2025, 9, 15),
        "title": "Balancing Code and Music",
        "excerpt": "How coding and music feed each other in my day-to-day.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.
        """
    },
    {
        "slug": "my-musical-journey",
        "image": "me-drumming.png",
        "author": "Dario",
        "date": date(2024, 5, 10),
        "title": "My Musical Journey",
        "excerpt": "From the first drum hits to today: why rhythm shapes how I learn and build.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.
        """
    },
    {
        "slug": "my-gig-with-heat",
        "image": "heat-gig.png",
        "author": "Dario",
        "date": date(2023, 11, 20),
        "title": "My Gig with HEAT",
        "excerpt": "Notes from the stage: what a live show taught me about focus and flow.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe similique velit nisi ad perspiciatis beatae quo repudiandae et inventore sed eligendi minima maxime reprehenderit nostrum, maiores architecto minus laborum in.
        """
    }
]


def get_date(post):
    return post["date"]

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
