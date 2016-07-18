from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from SalesManagement.models import Customer, Seller, Product

@login_required(login_url='/sales/login')
def test(request):
	return render(request, 'SalesManagement/testing.html',{'username':'kiriti'})


def test1(request):
    return render(request, 'updated.html')

#To authenticate the user manually. Alternate way is to use django provided view.
def authenticate_user(request):

    if request.method == "POST":    #This case occurs when the form is being submitted.
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == "customer":
            obj = Customer.objects.filter(customer_email = email)
        else:
            obj = Seller.objects.filter(seller_email = email)

        if len(obj) == 0: #Invalid email
            return render(request,'SalesManagement/login.html',{'message':'Email Invalid, please try again'})
        elif len(obj) > 1: #Duplicate email
            return render(request,'SalesManagement/login.html',{'message':'Duplicate email, please check'})
        else:   #Check the password
            if role == "customer":
                redirect_url = 'customer-details'
                original_password = obj[0].customer_password
            else:
                redirect_url = 'seller-details'
                original_password = obj[0].seller_password

            if original_password == password:
                return redirect(reverse_lazy(redirect_url, kwargs= { 'pk' : obj[0].pk}))
            else:   #Wrong password
                return render(request,'SalesManagement/login.html',{'message':'Password Incorrect!!'})
    else:
        return render(request,'SalesManagement/login.html')    #This case occurs when the URL is typed in the address bar.


def logout_view(request):
    logout(request)
    return render(request,'SalesManagement/login.html',{'message':'Logged out successfully, enter the details below to login again'})


class CustomerCreate(View):
    def get(self, request):
        return render(request, 'SalesManagement/customer_create1.html')

    def post(self, request):
        name = request.POST.get('customer_name')
        address = request.POST.get('customer_address')
        email = request.POST.get('customer_email')
        phone = request.POST.get('customer_phone')
        password = request.POST.get('customer_password')
        c = Customer(customer_name = name, customer_adress = address, customer_email = email, customer_phone = phone, customer_password = password)
        c.save()

        return redirect(reverse_lazy('customer-details', kwargs= { 'pk' : c.pk}))


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


class SellerCreate(View):
    def get(self, request):
        return render(request, 'SalesManagement/seller_create1.html')

    def post(self, request):
        name = request.POST.get('seller_name')
        address = request.POST.get('seller_address')
        email = request.POST.get('seller_email')
        phone = request.POST.get('seller_phone')
        password = request.POST.get('seller_password')
        c = Seller(seller_name = name, seller_address = address, seller_email = email, seller_phone = phone, seller_password = password)
        c.save()

        return redirect(reverse_lazy('seller-details', kwargs= { 'pk' : c.pk}))

class CustomerDetailsView(DetailView):
    model= Customer
    template_name = 'SalesManagement/customer_details1.html'
    context_object_name = 'cust'


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'prod'


class SellerDetailsView(DetailView):
    model=Seller
    template_name = 'SalesManagement/seller_details1.html'
    context_object_name = 'sell'

class CustomerUpadateView(UpdateView):
    model = Customer
    fields = ['customer_adress',
        'customer_email',
    'customer_phone',]


    def get_success_url(self):
       return reverse_lazy('customer-details', kwargs= { 'pk' : self.object.pk} )


class ProductUpdateView(UpdateView):
    # def get(self, request):
    #     return render(request, 'SalesManagement/product_update_form.html')

    # def post(self, request, product_id):
    #     price = request.POST.get('product_price')
    #     discount = request.POST.get('product_discount')
    #     count = request.POST.get('product_count')
        
    #     #Get the object based on product_id and edit the details and save the object
    #     p = Product.objects.get(pk = product_id)
    #     p.product_price = price
    #     p.product_discount = discount
    #     p.product_count = count
    #     p.save()

    #     return redirect( reverse_lazy(('product-details'), kwargs= {'pk' : p.pk}) )
    
    model = Product
    fields = ['product_price',
              'product_discount',
              'product_count',
    ]

    def get_success_url(self):
        return reverse_lazy('product-details', kwargs= {'pk' : self.object.pk} )

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
    template_name = 'SalesManagement/product_list1.html'

class CustomerProductList(ListView):
    model = Product
    template_name = 'SalesManagement/product_customer.html'
