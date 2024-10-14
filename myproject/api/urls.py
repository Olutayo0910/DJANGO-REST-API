from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view(), name='product-update'),
    path('products/list/', views.ProductListView.as_view(), name='product-list'),
    path('products/search/', views.ProductList.as_view(), name='product-search'),
]
