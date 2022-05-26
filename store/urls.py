
from django.contrib import admin
from django.urls import path
from store.middleware.auth import Auth_middleware
from store.store_views import home,register,login,logout, cart, checkout, orders

urlpatterns = [
    path('',  home.Index.as_view(), name="homepage"),
    path('register',  register.Register.as_view(), name="register"),
    path('login',  login.Login.as_view(), name="login"),
    path('logout',  logout.Logout.as_view(), name="logout"),
    path('cart',  cart.Cart.as_view(), name="cart"),
    path('check-out',  checkout.Checkout.as_view(), name="checkout"),
    path('orders',  Auth_middleware(orders.OrderView.as_view()), name="orders"),
]
