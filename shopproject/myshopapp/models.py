from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    location = models.TextField(max_length=1000)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    entry_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='products/')

    def __str__(self):
        return f'{self.title} - {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: dated {self.order_date} by {self.client}'
