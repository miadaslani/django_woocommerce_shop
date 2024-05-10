from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from shop.models import Name , Product
from .forms import *
from accounts.models import Counseling

#-----------------------------صفحه اصلی
def main_page(request):
    name_record = Name.objects.all()
    product_record = Product.objects.all()
    if request.method == 'POST':
        form_counseling = CounselingForm(request.POST)
        if form_counseling.is_valid():
            data = form_counseling.cleaned_data
            phone_number = data['phone_number']
            Counseling.objects.get_or_create(number=phone_number)
            return HttpResponse("در اسرع وقت باهاتون تماس میگیریم")
    else:
        form_counseling = CounselingForm()
    return render(request, "mezonaslani/index.html",{"a":name_record,"product":product_record,"form":form_counseling})


def dynamic_mezonaslani(request, mezonaslani):
    return HttpResponseNotFound(f"{mezonaslani}-- PAGE NOT FOUND")

 
