from django.db import models

# Модель Клиент
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    registration_date = models.DateField()

    def __str__(self):
        return self.name

# Модель Товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    adding_date = models.DateField()

    def __str__(self):
        return self.name

# Модель Заказ
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f"Order #{self.pk}"

# Пример функций CRUD

# Создание клиента
def create_client(data):
    client = Client.objects.create(**data)
    return client

# Получение всех клиентов
def get_all_clients():
    clients = Client.objects.all()
    return clients

# Обновление клиента
def update_client(client_id, data):
    client = Client.objects.get(id=client_id)
    client.name = data['name']
    client.email = data['email']
    client.phone_number = data['phone_number']
    client.address = data['address']
    client.registration_date = data['registration_date']
    client.save()
    return client

# Удаление клиента
def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()

# Создание товара
def create_product(data):
    product = Product.objects.create(**data)
    return product

# Получение всех товаров
def get_all_products():
    products = Product.objects.all()
    return products

# Обновление товара
def update_product(product_id, data):
    product = Product.objects.get(id=product_id)
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.quantity = data['quantity']
    product.adding_date = data['adding_date']
    product.save()
    return product

# Удаление товара
def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

# Создание заказа
def create_order(data):
    client = Client.objects.get(id=data['client_id'])
    products = Product.objects.filter(id__in=data['product_ids'])
    total_amount = sum([product.price for product in products])
    order = Order.objects.create(client=client, total_amount=total_amount, order_date=data['order_date'])
    order.products.set(products)
    return order

# Получение всех заказов
def get_all_orders():
    orders = Order.objects.all()
    return orders

# Обновление заказа
def update_order(order_id, data):
    order = Order.objects.get(id=order_id)
    order.client = Client.objects.get(id=data['client_id'])
    products = Product.objects.filter(id__in=data['product_ids'])
    total_amount = sum([product.price for product in products])
    order.products.set(products)
    order.total_amount = total_amount
    order.order_date = data['order_date']
    order.save()
    return order

# Удаление заказа
def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()