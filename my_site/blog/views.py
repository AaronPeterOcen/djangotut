# from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import Post


# all_posts = [
# ]

def get_date(post):
    return post["date"]
# from django.http import HttpResponse
# Create your views here.

def index(request, slug):
    latest_posts = get_object_or_404(Post, slug=slug)
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html", {
        "posts": latest_posts
    })

    # pass

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })

def post_detail(request, slug):
    # id_post = next(post for post in all_posts if post["slug"] == slug)
    id_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post
    })
