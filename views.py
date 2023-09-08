from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from my_app import Client, Product, Order


def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    today = timezone.now().date()
    week_start_date = today - timedelta(days=7)
    month_start_date = today - timedelta(days=30)
    year_start_date = today - timedelta(days=365)

    # Получаем товары, заказанные клиентом за последнюю неделю
    latest_week_products = Product.objects.filter(order__client=client, order__order_date__gte=week_start_date).distinct()

    # Получаем товары, заказанные клиентом за последний месяц
    latest_month_products = Product.objects.filter(order__client=client, order__order_date__gte=month_start_date).distinct()

    # Получаем товары, заказанные клиентом за последний год
    latest_year_products = Product.objects.filter(order__client=client, order__order_date__gte=year_start_date).distinct()

    context = {
        'client': client,
        'latest_week_products': latest_week_products,
        'latest_month_products': latest_month_products,
        'latest_year_products': latest_year_products
    }
    return render(request, 'orders.html', context)
