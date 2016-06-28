from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpRequest

from SalesManagement.models import Customer, Seller, Product


def test(request):
    return render(request, 'hello.html')

def test1(request):
    return render(request, 'updated.html')

class CustomerCreate(CreateView):
    model =  Customer
    fields =  [  'customer_name',
    'customer_adress',
    'customer_email',
    'customer_phone',
                 ]

    def get_success_url(self):
        return reverse_lazy('customer-details' , kwargs= { 'pk' : self.kwargs['pk'] })

class ProductCreate(CreateView):
    model = Product
    fields = ['product_name',
    'product_seller',
    'product_discount',
    'product_price',
    'product_count',
              ]

    def get_success_url(self):
        return reverse_lazy('product-list')


class SellerCreate(CreateView):
    model = Seller
    fields = ['seller_name',
    'seller_address',
    'seller_email',
    'seller_phone',]


    def get_success_url(self):
        return reverse_lazy('hello')
        # return super(CustomerCreate, self).get_success_url()

class CustomerDetailsView(DetailView):
    model= Customer
    context_object_name = 'cust'


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'prod'


class SellerDetailsView(DetailView):
    model=Seller
    context_object_name = 'sell'

class CustomerUpadateView(UpdateView):
    model = Customer
    fields = ['customer_adress',
        'customer_email',
    'customer_phone',]


    def get_success_url(self):
        temp_pk = self.kwargs['pk']
        temp_url = "127.0.0.1:8000/sales/customer/details/"
        return reverse(temp_url)
    # return super(CustomerCreate, self).get_success_url()

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_price',
              'product_discount',
              'product_count',
              ]

    def get_success_url(self):
        return reverse_lazy('product-details')

class ProductDeleteView(DeleteView):
    model = Product
    fields = ['product_name', 'product_price' , 'product_discount', 'product_count']
    success_url = reverse_lazy('product-list')
    # def get_success_url(self):
     #   return reverse_lazy('product-list')


class SellerUpdateView(UpdateView):
    model = Seller
    fields = ['seller_name',
    'seller_address',
    'seller_email',
    'seller_phone',]

    def get_success_url(self):
        return reverse_lazy('updated')



class ProductList(ListView):
    model= Product
