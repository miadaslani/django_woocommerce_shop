from django.contrib import admin
from .models import *
from bidi.algorithm import get_display
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    lst_display = ['name']
    prepopulated_fields = {'slug':['name']}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','manufacture','price']
    list_filter = ['price']
    list_editable = ['price']
    prepopulated_fields = {'slug':['name','description','manufacture']}







admin.site.register(Name)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Customer)
admin.site.register(Manufacture)

