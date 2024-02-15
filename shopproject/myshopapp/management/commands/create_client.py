from django.core.management.base import BaseCommand

from myshopapp.models import Client


class Command(BaseCommand):
    help = "Create 5 fake clients."

    def handle(self, *args, **options):
        clients = [Client(name='John Doe',
                          email='j_doe@email.zz',
                          phone_number='+71002003040',
                          location='Moscow, Russia'),
                   Client(name='Jane Doe',
                          email='jane_doe@email.hh',
                          phone_number='+71002013141',
                          location='Moscow, Russia'),
                   Client(name='Ken Miles',
                          email='miles@master.uk',
                          phone_number='+441001001010',
                          location='London, UK'),
                   Client(name='Ann Russo',
                          email='a_russo@mail.ll',
                          phone_number='+91001001010',
                          location='Quebec, Canada'),
                   Client(name='Elona Prost',
                          email='prost@randmail.qq',
                          phone_number='+91009991010',
                          location='Beijing, PRC')
                   ]
        for client in clients:
            client.save()
            self.stdout.write(f'{client}')
