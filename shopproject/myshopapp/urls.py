from django.conf.urls.static import static
from django.urls import path

from shopproject import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('task3/', views.task3, name='task3'),
    path('client/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/products/', views.client_products, name='client_products'),
    path('task4/', views.task4, name='task4'),
    path('product/<int:product_id>/change/', views.product_change, name='product_change'),
    path('product/add/', views.product_add, name='product_add'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
