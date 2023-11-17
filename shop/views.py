import json
from math import ceil

from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact, Order, OrderUpdate, Product


# Create your views here.
def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id', 'price')
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
    if request.method=="POST":
        orderId = request.POST.get('OrderID', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)  # noqa: E501
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception:
            return HttpResponse('{"status":"error"}')
    else:
        products = Product.objects.values('product_name', 'price')
        total_price = 0
        for product in products:
            
            total_price += product['price']
        
        return render(request, "shop/tracker.html", {'total_price': total_price})
    

def searchMatch(query, item):
    if query.lower() in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower(): # noqa: E501
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        producttemp = Product.objects.filter(category=cat)
        product = [item for item in producttemp if searchMatch(query, item)]

        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(product) != 0:
            allProds.append([product, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "No Results Found. Please Check Your Query and Try Again."}
    return render(request, 'shop/search.html', params)

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    
    return render(request, "shop/prodview.html", {'product': product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')

        address = request.POST.get('address1', '') + " " + request.POST.get(
            'address2', '')  

        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Order(items_json=items_json, name=name, email=email, address=address,
         city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)

        order.save()

        update = OrderUpdate(order_id=order.order_id,
        update_desc="The order has been placed.")

        update.save()

        thank = True

        id = order.order_id

        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    
    else:
        products = Product.objects.values('product_name', 'price')
        total_price = 0
        for product in products:
            
            total_price += product['price']
        
        return render(request, "shop/checkout.html", {'total_price': total_price})







#               QUIZ 
# def login(request):
#   return HttpResponse("We r at login")

# def signup(request):
#   return HttpResponse("We r at signup")



#            EXERCISE
# from .models import Product

# def index(request):
#    products = Product.objects.all()
#    context = {'products': products}
#    return render(request, 'shop/index.html', context)
