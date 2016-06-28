from django.contrib import admin

# Register your models here.
from SalesManagement.models import Customer,Product,Seller
admin.site.register([Customer,Product,Seller])
