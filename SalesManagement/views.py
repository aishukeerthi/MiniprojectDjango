from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

# Create your views here.
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                #Redirect to a success page
                return redirect('product-list')
            else:
                #Return a disabled account message
                return render(request,'SalesManagement/login.html',{'message':'Account disabled, try another account'})    
        else:
            return render(request,'SalesManagement/login.html',{'message':'Details invalid, please try again'})
        #return render(request,'SalesManagement/testing.html',{'username':username, 'password':password},content_type='html')
    else:        
        return render(request,'SalesManagement/login.html')    #This case occurs when the URL is typed in the address bar.


def add_to_cart(request, product_id, quantity):
    product_id = request.POST.get('id',1)
    product = Product.objects.get(id=int(product_id))
    quantity = request.POST.get('quantity',1)

    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request,'SalesManagement/cart.html', {'cart':Cart(request)})

def logout_view(request):
    logout(request)
    return render(request,'SalesManagement/login.html',{'message':'Logged out successfully, enter the details below to login again'})


class CustomerCreate(CreateView):
    model =  Customer
    fields =  [  'customer_name',
    'customer_adress',
    'customer_email',
    'customer_phone',
                 ]

    #The object that is just created can be accessed by 'self.object'
    def get_success_url(self):
        return reverse_lazy('customer-details' , kwargs= { 'pk' : self.object.pk})

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
        return reverse_lazy('seller-details', kwargs= { 'pk' : self.object.pk} )
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
       return reverse_lazy('customer-details', kwargs= { 'pk' : self.object.pk} )


class ProductUpdateView(UpdateView):
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
    template_name = 'SalesManagement/product_seller.html'

class CustomerProductList(ListView):
    model = Product
    template_name = 'SalesManagement/product_customer.html'
