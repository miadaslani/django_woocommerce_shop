from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from shop.models import Name
# Create your views here.

#-----------------------------register
def viewRegister(request):
    if request.method=='POST':
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password_2'])
            
            return HttpResponse('Successfully')
    else:
        form_register=UserRegisterForm()
    if request.user.is_authenticated:
        a = Name.objects.all()
        return render (request, 'accounts/index.html',{'a':a})
    return render(request, 'accounts/signup.html',{'form_register':form_register})


#------------------------login
def viewLogin(request):
    if request.method=='POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            user=authenticate(request,username=data['user'],password=data['password'])
            if user:
                login(request,user)
                return HttpResponse('done') 
    else:
        form_login=UserLoginForm()
    if request.user.is_authenticated:
        a = Name.objects.all()
        return render(request, 'accounts/index.html',{'a':a})
    return render(request,'accounts/signin.html',{'form_login':form_login})


#------------------------logout
def viewLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('done logout')
    else:
        return HttpResponse('شما هنوز وارد اکانتی نشده اید')


#--------------------------change password user
@login_required
def viewChangePassword(request):
    if request.method == 'POST':
        user = request.user
        form=UserChangePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            old_password = data['old_password']
            new_password1 = data['new_password1']
            new_password2 = data['new_password2']
            if not user.check_password(old_password):
                return HttpResponse("رمز اشتباه میباشد")
            elif new_password1 != new_password2:
                return HttpResponse("رمز ها باهم یکی نیست")
            else:
                user.set_password(new_password1)
                login(request,user)
                user.save()
                return HttpResponse("رمز با موفقیت عوض شد")
    else:
        form=UserChangePasswordForm()
    return render(request, 'accounts/changepassword.html',{'form':form})


