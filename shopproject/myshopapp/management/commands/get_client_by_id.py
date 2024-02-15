from django.core.management.base import BaseCommand

from myshopapp.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **options):
        pk = options['pk']
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            self.stdout.write(f'{client}')
        else:
            self.stdout.write(f'Client not found.')
