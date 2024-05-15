from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

#-------------------------- navbar مدل تغییر اسم بالای صفحه
class Name(models.Model):
    name1=models.CharField(max_length=30,verbose_name='صفحه اصلی')
    name2=models.CharField(max_length=30,verbose_name='درباره ما')
    name3=models.CharField(max_length=30,verbose_name='محصولات')
    name4=models.CharField(max_length=30,verbose_name='صفحات')
    name5=models.CharField(max_length=30,verbose_name='وبلاگ')
    name6=models.CharField(max_length=30,verbose_name='تماس با ما')
    logo=models.ImageField(upload_to='images/photo',verbose_name='لوگو')
                                                
    class Meta:
        verbose_name='اسم'
        verbose_name_plural='اسم ها'

#----------------------------------مدل برند محصول
class Brand(models.Model):
    name =models.CharField(max_length=50,verbose_name='نام برند')
    slug =models.SlugField(default='',null=False,db_index=True,verbose_name='اسلاگ')


    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'

    def __str__(self):
        return self.name
#-----------------------مدل سازنده ها
class Manufacture(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام سازنده')
    class Meta:
        verbose_name='سازنده'
        verbose_name_plural='سازنده ها'
     
    def __str__(self):
        return self.name

#------------------------مدل مشتری ها
class Customer(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام مشتری')
    slug=models.SlugField(default='',null=False,db_index=True,verbose_name='اسلاگ')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name+'-'+self.description)
        super().save(*args,**kwargs)

    class Meta:
        verbose_name='مشتری'
        verbose_name_plural='مشتری ها'

    def __str__(self):
        return self.name



#------------------------------------مدل محصولات
class Product(models.Model):
    name = models.CharField(max_length=40,verbose_name='نام محصول')
    brand=models.OneToOneField(Brand,on_delete=models.CASCADE,null=True,blank=True,verbose_name='نام برند')
    manufacture=models.ForeignKey(Manufacture,on_delete=models.CASCADE,null=True,blank=True,verbose_name='نام سازنده')
    customer=models.ManyToManyField(Customer,verbose_name='مشتری')
    description = models.CharField(max_length=500, default='', blank=True, null=True,verbose_name='کپشن')
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12,verbose_name='قیمت')
    picture = models.ImageField(upload_to='images/photo/',verbose_name='عکس')
    is_sale = models.BooleanField(default=False,verbose_name='آیا این محصول تخفیف دارد؟')
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12,verbose_name='قیمت تخفیف')
    slug=models.SlugField(default='',null=False,db_index=True,verbose_name='اسلاگ')

    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name+'-'+self.description)
        super().save(*args,**kwargs)


    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'

    def __str__(self):
        return f'{self.name}----{self.description}'

#--------------------مدل سبد خرید
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.product.name
    
