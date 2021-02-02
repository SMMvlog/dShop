from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from store.models.product import Product


class Cart(View):
    def get(self,request):
            a=list(request.session.get("cart").keys())
            # b=request.session.get("cart")
            # b=list(request.session.get("cart").values())
            # print(a)
            # print(b)
            products = Product.objects.filter(id__in=a)
            # print(products) 
            return render(request,"cart.html",{"products":products})
            