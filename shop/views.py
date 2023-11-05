from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.
def index(request):
#    products = Product.objects.all()
#    print(products)
    

    # params = {"no_of_slides": nSlides, 'range': range(1, nSlides), "product": products}

    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])

    #allProds = [
     #   [products, range(1, nSlides), nSlides],
      #  [products, range(1, nSlides), nSlides]
       # ]
    params = {
        "allProds": allProds
        }
    return render(request, "shop/index.html", params)




def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def productView(request, myid):
    # fetch the project using the ID
    product = Product.objects.filter(id=myid)
    
    return render(request, "shop/prodview.html", {'product': product[0]})

def checkout(request):
    return render(request, "shop/checkout.html")

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