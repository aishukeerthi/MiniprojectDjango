from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^hello/$',views.test,name='hello'),
    url(r'^updated/$', views.test1, name='updated'),
    url(r'^product/list/$', views.ProductList.as_view(), name= 'product-list'),
    url(r'^customer/create/$', views.CustomerCreate.as_view(),name='customer-create'),
    url(r'^seller/create/$', views.SellerCreate.as_view(), name='seller-create'),
    url(r'^product/create/$', views.ProductCreate.as_view(), name='product-create'),
    url(r'^customer/(?P<pk>[0-9]+)/details/$', views.CustomerDetailsView.as_view(), name = 'customer-details'),
    url(r'^product/(?P<pk>[0-9]+)/details/$', views.ProductDetailsView.as_view(), name='product-details'),
    url(r'^seller/(?P<pk>[0-9]+)/details/$', views.SellerDetailsView.as_view(), name='seller-details'),
    url(r'^customer/(?P<pk>[0-9]+)/update/$', views.CustomerUpadateView.as_view(), name='customer-Update'),
    url(r'^seller/(?P<pk>[0-9]+)/update/$', views.SellerUpdateView.as_view(), name='seller-Update'),
    url(r'^product/(?P<pk>[0-9]+)/update/$', views.ProductUpdateView.as_view(), name='product-update'),
    url(r'^product/(?P<pk>[0-9]+)/delete/$', views.ProductDeleteView.as_view(), name='product-delete'),
]