from datetime import date

from django.shortcuts import render


posts = [
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
        "date": date(2024, 3, 5),
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
        "date": date(2024, 3, 5),
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
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"blog/index.html")
    # pass

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")