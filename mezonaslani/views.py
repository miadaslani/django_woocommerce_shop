from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from shop.models import Name

def main_page(request):
    name_record = Name.objects.all()
    return render(request, "mezonaslani/index.html",{"a":name_record})


def dynamic_mezonaslani(request, mezonaslani):
    return HttpResponseNotFound(f"{mezonaslani}-- PAGE NOT FOUND")


