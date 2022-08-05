from distutils.command.upload import upload
from enum import unique
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300)
    icon = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length= 300)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    slug = models.CharField(max_length= 300)
    icon = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to = 'media')
    icon = models.TextField(blank =True)
    url = models.URLField(blank = True)

    def __str__(self):
        return self.name

class Ads(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to = 'media')
    rank = models.ImageField(unique = True)
    description = models.TextField(blank = True)


    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to= 'media')
    rank = models.ImageField(unique = True)

    def __str__(self):
        return self.name
STOCK =(( 'In','In Stock'),('Out','Out stock'))
LABELS = (('hot','hot'),('sale','sale'),('new','new'),('','defult'))
class Product(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to= 'media')
    price = models.IntegerField(default=0)
    discont_price = models.IntegerField(default=0)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
    stock = models.CharField(choices = STOCK,max_length=20)
    lables = models.CharField(choices = LABELS,blank= True,max_length=20)
    description = models.TextField(blank = True)
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name

