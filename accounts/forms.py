from django import forms 
from django.contrib.auth.models import User


#---------------------------------- form register 
class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری را وارد کنید'}))
    email=forms.CharField(max_length=20,widget=forms.EmailInput(attrs={'placeholder':'برای مثال:test@gmail.com'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'لطفا اسمتون رو وارد کنید'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'لطفا نام خانوادگیتون رو وارد کنید'}))
    password_1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'لطفا یک رمز وارد کنید'}))
    password_2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'رمز را مجدد وارد کنید'}))
 
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است')
        return user
    
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده ')
        return email
    
    def clean_password_2(self):
        pass1=self.cleaned_data['password_1']
        pass2=self.cleaned_data['password_2']
        if pass1!=pass2:
            raise forms.ValidationError("رمز ها باهم مطابق نیستند")
        elif len(pass2)<8:
            raise forms.ValidationError('رمز نباید کوچکتر از 8 کاراکتر باشد')
        elif not any(i.isupper() for i in pass2):
            raise forms.ValidationError("رمز باید دارای حداقل یک حرف بزرگ باشد")
        return pass2
    
#----------------------------------form login
class UserLoginForm(forms.Form):
    user=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری را وارد کنید'}))
    password=forms.CharField(widget=forms.PasswordInput())

class UserChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())
