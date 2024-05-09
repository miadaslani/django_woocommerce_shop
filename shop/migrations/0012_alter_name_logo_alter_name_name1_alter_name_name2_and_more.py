# Generated by Django 5.0.2 on 2024-04-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_brand_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='logo',
            field=models.ImageField(upload_to='images/photo', verbose_name='لوگو'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name1',
            field=models.CharField(max_length=30, verbose_name='صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name2',
            field=models.CharField(max_length=30, verbose_name='درباره ما'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name3',
            field=models.CharField(max_length=30, verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name4',
            field=models.CharField(max_length=30, verbose_name='صفحات'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name5',
            field=models.CharField(max_length=30, verbose_name='وبلاگ'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name6',
            field=models.CharField(max_length=30, verbose_name='تماس با ما'),
        ),
    ]
