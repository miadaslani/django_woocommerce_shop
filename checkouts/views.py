from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from shop.models import Cart,Product
from .models import *
from .forms import *
# Create your views here.

#-------------------------صفحه پرداخت
def Checkout(request):
    if Cart.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            
            
                form = CheckOutForm(request.POST)
                cart_items = Cart.objects.filter(user=request.user).prefetch_related('products')
                products = [product for cart_item in cart_items for product in cart_item.products.all()]
                if form.is_valid():
                    data = form.cleaned_data
                    CheckOut.objects.create(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    phone_number = data['phone_number'],
                    email = data['email'],
                    address = data['address'],
                    city = data['city'],
                    zipcode = data['zipcode'],
                    
                    )
                    
                    
                
                    cart_items = Cart.objects.filter(user=request.user)
                    paid_product = [PaidProduct(user=request.user, product=product) for cart_item in cart_items for product in cart_item.products.all()]
                    PaidProduct.objects.bulk_create(paid_product)
                    cart_items.delete()
                    return HttpResponse(" سفارش شما با موفقیت ثبت شد لطفا به این شماره پیام بدید تا فرآیند پرداخت انجام شود 09912240717")
        else:            
            form = CheckOutForm()
            cart_items = Cart.objects.filter(user=request.user).prefetch_related('products')
            products = [product for cart_item in cart_items for product in cart_item.products.all()] 
            initial_data = {
                         'first_name':request.user.first_name,
                         'last_name':request.user.last_name,
                    }
            form = CheckOutForm(initial=initial_data)
    else:
         return HttpResponse("سبد خرید شما خالی است")  
    
    return render(request, 'checkouts/checkout.html',{"cart":products,"form":form})


