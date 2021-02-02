from django import views
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Index(View):
    def get(self,request):
        cat=Category.objects.all()
        categoryID = request.GET.get('cat')
        if categoryID:
            pro = Product.objects.filter(category=categoryID)
        else:
            pro=Product.objects.all()
        data = {'pro':pro,'cat':cat} 
        return render(request,'index.html',data)

    def post(self,request):
        i = request.POST.get('id')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(i)
            if quantity:
               cart[i]=quantity+1
            else:
                cart[i]=1
        else:
            cart = {}
            cart[i]=1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('index')




    