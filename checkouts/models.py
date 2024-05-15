from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.


class CheckOut(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()

    class Meta:
        verbose_name='آدرس ها'
        verbose_name_plural='آدرس صورت حساب'
    

    


class PaidProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='پرداخت ها'
        verbose_name_plural='محصولات پرداخت شده'

    def __str__(self):
        return f"{self.user.username}  -   {self.product.name}  -  {self.payment_date}"
