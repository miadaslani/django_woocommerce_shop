from . import views
from django.urls import path

urlpatterns = [
    path("",views.listofmonth),
    path("<str:months>", views.dynamic_month),
    

]