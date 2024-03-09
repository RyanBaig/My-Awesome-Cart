from django.contrib import admin

# Register your models here.
from .models import Contact, Order, OrderUpdate, Product

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)