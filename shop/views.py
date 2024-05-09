from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from .models import *
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.views import *


# Create your views here.


#-------------------تمرین های کلاسی
days = {
    "monday": "this is monday",
    "tuesday": "this is tuesday",
    "wednesday": "this is wednesday",
    "tuersday": "this is tuersday",
    "friday": "this is friday",
    "saturday": "this is saturday",
    "sunday": "this is sunday",
}


# def python(request):
# return HttpResponse("<font size='20'><p style='color:blue'>python is very easy</p></font>")


# def program(request):
# a = "<font size='20'><ul><li>python</li><li>django</li><li>data sciense</li></ul></font>"
# return HttpResponse("list of python: <br>" + a)


# def dynamic_shop(request, shop,description):
# return HttpResponse(f"{shop}-And-{description}-- PAGE NOT FOUND")


#---------------------------app  نمایش صفحه اولیه   
def woocommerce(request):
    name_record=Name.objects.all()
    product_record = Product.objects.all()
    return render(request, "shop/product_list.html", {"a":name_record,"product_record":product_record})



#-------------------تمرین های کلاسی
def dynamic_shop_keys(request, shop):

    data = list(days.keys())
    if shop > len(data) or shop == 0:
        return HttpResponse("PAGE NOT FOUND")
    redirect_shop = data[shop - 1]
    return HttpResponseRedirect(f"/shop/{redirect_shop}")

#-------------------تمرین های کلاسی
def dynamic_shop(request, shop):
    data = days.get(shop)
    if data:
        return HttpResponse(f"{shop}:{data}-- PAGE  FOUND")
    return HttpResponseNotFound(f"{shop}-- NOT FOUND")

#-------------------تمرین های کلاسی
def listofdays(request):
    a = list(days.keys())
    b = ""
    for i in a:
        b += f"<ul><li><a href='{i}'</a>{i}</li></ul>"

    return HttpResponse(b)

# def viewName(request):
#     Name_record=Name.objects.all()
#     return render(request, 'shop/product_list.html', {'name_record':Name_record})

#------------------------جزییات محصولات
def viewNameDetails(request,s):
    name_details = get_object_or_404(Product,slug=s)
    return render(request, 'shop/single-product.html',{'name_details':name_details})

#---------------------------------تابع افزودن محصول به سبد خرید
def add_to_cart(request):
    if request.method == "POST":
            if request.user.is_authenticated:
                product_id = request.POST.get('product_id')
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    return HttpResponse('محصول مورد نظر یافت نشد')
                
                cart, created = Cart.objects.get_or_create(user=request.user)
                cart.products.add(product)
                return HttpResponse('محصول با موفقیت به سبد خرید اضافه شد')
            else:
                return HttpResponse('لطفا یک حساب کاربری بسازید و وارد آن شوید')

    else:
        return HttpResponse('اطلاعات ارسال شده نامعتبر است')
    
#----------------------تابع نمایش سبد خرید
def cart_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        total_price = 0
        if cart:
            for product in cart.products.all():
                total_price += product.price
        return render(request, 'shop/cart.html',{'cart':cart,'total_price':total_price})
    else:
        return HttpResponse('لطفا یک حساب کاربری بسازید و وارد آن شوید سپس مجدد امتحان کنید')
    









# def name1(request):
