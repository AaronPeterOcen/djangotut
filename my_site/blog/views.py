from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"blog/index.html")
    # pass

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request):
    pass