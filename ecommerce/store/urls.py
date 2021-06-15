from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.store, name='cart'),
    path('checkout', views.store, name='checkout'),
]
