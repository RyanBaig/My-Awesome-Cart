from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
# def index(request):
#     return render(request, "blog/index.html")

def blogpost(request):
    return render(request, "blog/blogpost.html")

#                      EXERCISE
def index(request):
    allPosts = []
    posts = Blogpost.objects.values('title', 'chead0', 'pub_date', 'thumbnail', 'post_id')
    # put all the different posts in a list
    allPosts.append(posts)
    print(allPosts)
    return render(request, 'blog/index.html', {'posts': allPosts[0]})
    