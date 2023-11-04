from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))

    params = {"no_of_slides": nSlides, 'range': range(1, nSlides), "product": products}
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("We r at contact")

def tracker(request):
    return HttpResponse("We r at tracker")

def search(request):
    return HttpResponse("We r at search")

def productView(request):
    return HttpResponse("We r at prodvuct view")

def checkout(request):
    return HttpResponse("We r at checkout")

#               QUIZ 
# def login(request):
#   return HttpResponse("We r at login")

# def signup(request):
#   return HttpResponse("We r at signup")



#            EXERCISE
# from .models import Product

#def index(request):
#    products = Product.objects.all()
#    context = {'products': products}
#    return render(request, 'shop/index.html', context)