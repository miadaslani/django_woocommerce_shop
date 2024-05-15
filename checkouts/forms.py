from django import forms


class CheckOutForm(forms.Form):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"placeholder":"نام"}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"placeholder":"نام خانوادگی"}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"شماره تلفن"}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={"placeholder":"ایمیل"}))
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"آدرس"}))
    city = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"placeholder":"شهر"}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"کد پستی"}))
    

    