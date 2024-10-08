from django.urls import path
from . import views

path('products/', views.ProductListCreate.as_view(), name='product-list-create')