from django.urls import path
from .views import Home, ProductList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products', ProductList.as_view(), name='product-list'),
]
