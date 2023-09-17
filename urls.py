from django.urls import path
from views import client_orders, add_product


app_name = 'orders'

urlpatterns = [
    path('client/<int:client_id>/', client_orders, name='client_orders'),
    path('add_product/', add_product, name='add_product'),
]