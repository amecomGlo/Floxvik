
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('products/', views.product_lists, name='product_lists'),
    path('<slug:slug>/', views.detail, name='detail'),
    
]
