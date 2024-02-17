from django.core.management.base import BaseCommand

from myshopapp.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **options):
        pk = options['pk']
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'Product not found.')
