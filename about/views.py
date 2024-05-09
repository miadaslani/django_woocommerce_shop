from django.shortcuts import render
from django.http import HttpResponse


def aboutme(request):
    return render(request, 'about/about.html')



def dynamic_about(request, about):
    return HttpResponse(f"{about}-- PAGE NOT FOUND")

