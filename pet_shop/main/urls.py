from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                     
    path('about/', views.about, name='about'),               
    path('cart/', views.cart, name='cart'),                  
    path('checkout/', views.checkout, name='checkout'),      
    path('confirmation/', views.confirmation, name='confirmation'),  
    path('contact/', views.contact, name='contact'),         
    path('login/', views.login, name='login'),               
    path('product_list/', views.product_list, name='product_list'),  
    path('single-product/', views.single_product, name='single-product'),
]
