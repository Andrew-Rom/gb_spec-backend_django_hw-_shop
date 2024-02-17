from django.core.management.base import BaseCommand

from myshopapp.models import Product


class Command(BaseCommand):
    help = "Change product price."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('price', type=str, help='Product price')

    def handle(self, *args, **options):
        pk = options.get('pk')
        price = options.get('name')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.price = price
            product.save()
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'Product not found.')
