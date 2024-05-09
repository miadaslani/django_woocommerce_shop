from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
month1 = {
    "january":"this is january",
    "february":"this is february",
    "March":"this is March",
    "april":"this is april",
    "may":"this is may",
    "june":"this is june",
    "july":"this is july",
    "august":"this is august",
}

def dynamic_month(request, months):
    data = month1.get(months)
    if data:
        return HttpResponse(f"{months}:{data}-- PAGE  FOUND")
    return HttpResponseNotFound(f"{months}-- NOT FOUND")

def listofmonth(request):
    a = 5
    b = 3 
    data = {'month':month1,"a":a,"b":b}
    return render(request, "month/month.html", context=data)
