from django.db import models
from mezonaslani.forms import CounselingForm
# Create your models here.

#---------------------------برای اپ مزون اصلانی صفحه اصلی
class Counseling(models.Model):
    number = models.CharField(max_length=20,verbose_name='شماره تماس')
    is_counseling = models.BooleanField(default=False,verbose_name='تایید پاسخگویی')

    class Meta:
        verbose_name='مشاوره'
        verbose_name_plural='مشاوره ها'