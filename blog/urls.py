# I have crreated this file - Ryan
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('post/<int:id>', views.blogpost, name="blogPost"),
    
]
