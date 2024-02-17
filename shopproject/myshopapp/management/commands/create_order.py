import random

from django.core.management.base import BaseCommand

from myshopapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Quantity of orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()
        for i in range(1, count + 1):
            client = random.choice(clients)
            order = Order(client=client, amount=0)
            order.save()
            for _ in range(1, count + 1):
                product = random.choice(products)
                if product.quantity > 0:
                    order.products.add(product)
                    order.amount += product.price
                    product.quantity -= 1
                    order.save()
            self.stdout.write(f'{order}')
