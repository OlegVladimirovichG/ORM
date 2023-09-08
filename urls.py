from django.urls import path
from views import client_orders

app_name = 'orders'

urlpatterns = [
    path('client/<int:client_id>/', client_orders, name='client_orders'),
]
d