from django.core.management.base import BaseCommand

from myshopapp.models import Client, Order


class Command(BaseCommand):
    help = "Get orders by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **options):
        pk = options['pk']
        orders = Order.objects.filter(client__pk=pk)
        text = '\n'.join(f'{order.products} - total amount {order.amount}'
                         for order in orders)
        self.stdout.write(text)
