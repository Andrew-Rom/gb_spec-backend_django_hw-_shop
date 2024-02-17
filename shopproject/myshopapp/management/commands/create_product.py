from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from myshopapp.models import Product


class Command(BaseCommand):
    help = "Create 12 fake products."

    def handle(self, *args, **options):
        products = [Product(title='Red Laptop',
                            description=lorem_ipsum.sentence(),
                            price=135777.01,
                            quantity=100),
                    Product(title='Red Smartphone',
                            description=lorem_ipsum.sentence(),
                            price=109000.99,
                            quantity=90),
                    Product(title='Red Earphone',
                            description=lorem_ipsum.sentence(),
                            price=9500.50,
                            quantity=80),
                    Product(title='Red Keyboard',
                            description=lorem_ipsum.sentence(),
                            price=1420.00,
                            quantity=70),
                    Product(title='Red Monitor',
                            description=lorem_ipsum.sentence(),
                            price=32700.01,
                            quantity=60),
                    Product(title='Red Mouse',
                            description=lorem_ipsum.sentence(),
                            price=1122.22,
                            quantity=50),
                    Product(title='Grey Laptop',
                            description=lorem_ipsum.sentence(),
                            price=115777.01,
                            quantity=50),
                    Product(title='Grey Smartphone',
                            description=lorem_ipsum.sentence(),
                            price=149000.99,
                            quantity=60),
                    Product(title='Grey Earphone',
                            description=lorem_ipsum.sentence(),
                            price=1500.50,
                            quantity=70),
                    Product(title='Grey Keyboard',
                            description=lorem_ipsum.sentence(),
                            price=3420.00,
                            quantity=80),
                    Product(title='Grey Monitor',
                            description=lorem_ipsum.sentence(),
                            price=12700.01,
                            quantity=90),
                    Product(title='Grey Mouse',
                            description=lorem_ipsum.sentence(),
                            price=2122.22,
                            quantity=100)
                    ]
        for product in products:
            product.save()
            self.stdout.write(f'{product}')
