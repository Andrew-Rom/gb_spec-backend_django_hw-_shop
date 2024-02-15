from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from myshopapp.models import Product


class Command(BaseCommand):
    help = "Create 12 fake products."

    def handle(self, *args, **options):
        products = [Product(title='Black Laptop',
                            description=lorem_ipsum.sentence(),
                            price=135777.01),
                    Product(title='Black Smartphone',
                            description=lorem_ipsum.sentence(),
                            price=109000.99),
                    Product(title='Black Earphone',
                            description=lorem_ipsum.sentence(),
                            price=9500.50),
                    Product(title='Black Keyboard',
                            description=lorem_ipsum.sentence(),
                            price=1420.00),
                    Product(title='Black Monitor',
                            description=lorem_ipsum.sentence(),
                            price=32700.01),
                    Product(title='Black Mouse',
                            description=lorem_ipsum.sentence(),
                            price=1122.22),
                    Product(title='White Laptop',
                            description=lorem_ipsum.sentence(),
                            price=115777.01),
                    Product(title='White Smartphone',
                            description=lorem_ipsum.sentence(),
                            price=149000.99),
                    Product(title='White Earphone',
                            description=lorem_ipsum.sentence(),
                            price=1500.50),
                    Product(title='White Keyboard',
                            description=lorem_ipsum.sentence(),
                            price=3420.00),
                    Product(title='White Monitor',
                            description=lorem_ipsum.sentence(),
                            price=12700.01),
                    Product(title='White Mouse',
                            description=lorem_ipsum.sentence(),
                            price=2122.22)
                    ]
        for product in products:
            product.save()
            self.stdout.write(f'{product}')
