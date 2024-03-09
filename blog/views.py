from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    
    return render(request, "blog/index.html", {'myposts': myposts})

def blogpost(request, id):
    # EXERCISE COMPLETED (ADD NEXT/PREVIOUS BUTTONS FOR POSTS)
    post = get_object_or_404(Blogpost, post_id=id)
    next_post = Blogpost.objects.filter(post_id=id + 1).first()
    prev_post = Blogpost.objects.filter(post_id=id - 1).first()

    # Check if next_post and prev_post exist
    if not next_post:
        next_post = "No New Posts..."
    if not prev_post:
        prev_post = "No Previous Posts..."
    
    return render(request, "blog/blogpost.html", {'post': post, 'next_post': next_post, 'prev_post': prev_post})

#                      EXERCISE
# def index(request):
    # allPosts = []
    # posts = Blogpost.objects.values('title', 'chead0', 'pub_date', 'thumbnail', 'post_id')

    # put all the different posts in a list

    # allPosts.append(posts)
    
    return render(request, 'blog/index.html', {'posts': allPosts[0]})
    