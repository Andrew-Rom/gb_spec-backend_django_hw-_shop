from django.core.management.base import BaseCommand

from myshopapp.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
