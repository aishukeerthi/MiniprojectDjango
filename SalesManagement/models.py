from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Seller(models.Model):
    seller_name=models.CharField(max_length=25)
    seller_address=models.CharField(max_length=25)
    seller_email=models.EmailField()
    seller_phone=models.CharField(max_length=10)

    def __str__(self):
        return self.seller_name

class Customer(models.Model):
    customer_name=models.CharField(max_length=25)
    customer_adress= models.CharField(max_length=40)
    customer_email=models.EmailField()
    customer_phone=models.CharField(max_length=10)
    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_name=models.CharField(max_length=25)
    product_seller=models.ForeignKey(Seller)
    product_discount=models.IntegerField(default=0)
    product_price=models.IntegerField()
    product_count=models.IntegerField()

    def __str__(self):
        return self.product_name
