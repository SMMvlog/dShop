from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.category import Category
# from store.models.product import Customer

class Checkoutview(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart= request.session.get('cart')
        # products= Product.get_products_by_id(list(cart.keys()))
        a = list(cart.keys())
        products = Product.objects.filter(id__in=a)
        print(address,phone,customer,products)

        for product in products:
            order = Order(category = Category(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            print(order)
            order.save()
        return redirect('cart')