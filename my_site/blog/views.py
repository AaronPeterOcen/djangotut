from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.png",
        "author": "Aaron",
        "date": date(2024, 3, 5),
        "title": "Mountain Hiking",
        "excerpt": """
        Theres nothing like the views you get when 
        hiking in the mountain! 
        And I wasn't even prepared for what happened while 
        I was enjoying the view!
        """,
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minima corporis laudantium doloremque, mollitia quisquam fugiat minus. 
        Pariatur eveniet laudantium sit eligendi dolorum, voluptates veritatis velit accusantium corrupti facere, qui doloremque?
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minima corporis laudantium doloremque, mollitia quisquam fugiat minus. 
        Pariatur eveniet laudantium sit eligendi dolorum, voluptates veritatis velit accusantium corrupti facere, qui doloremque?

        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minima corporis laudantium doloremque, mollitia quisquam fugiat minus. 
        Pariatur eveniet laudantium sit eligendi dolorum, voluptates veritatis velit accusantium corrupti facere, qui doloremque?
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minima corporis laudantium doloremque, mollitia quisquam fugiat minus. 
        Pariatur eveniet laudantium sit eligendi dolorum, voluptates veritatis velit accusantium corrupti facere, qui doloremque?
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Aaron",
        "date": date(2024, 2, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "fore.jpg",
        "author": "Aaron",
        "date": date(2023, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    }
]

def get_date(post):
    return post["date"]
# from django.http import HttpResponse

# Create your views here.

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html", {
        "posts": latest_posts
    })

    # pass

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })

def post_detail(request, slug):
    id_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post
    })