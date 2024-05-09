from django.urls import path
from . import views

urlpatterns =[
    path("",views.viewRegister,name='viewRegister'),
    path("login",views.viewLogin,name='viewLogin'),
    path("logout/",views.viewLogout,name='viewLogout'),
    path("cp/",views.viewChangePassword, name='viewChangePassword'),
]