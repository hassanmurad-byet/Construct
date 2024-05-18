from django.db import models

# Create your models here.


class aboutinfo(models.Model):
    title =models.CharField(max_length=100)
    des = models.CharField(max_length=200)
    about_image = models.ImageField(upload_to='all_img',verbose_name=("Image"), null=True, blank=True)
   

class whychoose(models.Model):
    title =models.CharField(max_length=100)
    des = models.CharField(max_length=200)

class ouerservice(models.Model):
    title = models.CharField(max_length=100)
    description =models.CharField(max_length=200)
    ser_image = models.ImageField(upload_to='all_img',verbose_name=("Image"), null=True, blank=True)


class customer(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    cust_image= models.ImageField(upload_to='all_img',verbose_name=("Image"), null=True, blank=True)


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=200)




    