from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('task3/', views.task3, name='task3'),
    path('client/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/products/', views.client_products, name='client_products'),
]
