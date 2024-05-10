from django import forms 



class CounselingForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'لطفا شماره تماستون رو وارد کنید'}))