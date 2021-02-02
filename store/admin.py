from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.signup import Signupm
from .models.orders import Order

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Signupm)
admin.site.register(Order)

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','description']

@admin.register(Signupm)
class signupmAdmin(admin.ModelAdmin):
    list_display = ['id','username','firstName','lastName','mobile','email','password1','password2']


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']