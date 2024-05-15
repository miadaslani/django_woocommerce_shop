from . import views
from django.urls import path


urlpatterns =[
    path("",views.Checkout,name='checkout'),
]