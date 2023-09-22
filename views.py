from django.shortcuts import get_object_or_404, render
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

from django.shortcuts import render, redirect
from .forms import ProductPhotoForm

def add_product(request):
    if request.method == 'POST':
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Замените 'product_list' на URL вашего списка продуктов
    else:
        form = ProductPhotoForm()

    return render(request, 'product_form.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})