# I have crreated this file - Ryan
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="BlogHome")
]
