from django.urls import path
from .views import PackageView, add_to_cart, CartView, reduce_from_cart, remove_from_cart, CheckoutView


urlpatterns = [
    path('', PackageView.as_view(), name='shop-view'),
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart'),
    path('reduce-from-cart/<id>/', reduce_from_cart, name='reduce-from-cart'),
    path('remove-from-cart/<id>/', remove_from_cart, name='remove-from-cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
