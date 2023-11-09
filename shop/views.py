from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from math import ceil
import json

# Create your views here.
def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])

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
    return render(request, "shop/contact.html", {"thank": True})

def tracker(request):
    if request.method == "POST":
        orderID = request.POST.get('OrderID', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderID, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderID)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception:
            pass
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    
    return render(request, "shop/prodview.html", {'product': product[0]})

def checkout(request):
    if request.method == "POST":

        items_json = request.POST.get('itemsJson', '{}')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phoneNumber', '')

        
        order = Order(name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, items_json=items_json)
        order.save()
        id = order.order_id
        update = OrderUpdate(order_id=id, update_desc="The order has been placed")
        update.save()
        thank = True
        
        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})
    else:
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