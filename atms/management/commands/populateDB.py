from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import requests
from atms.models import ATM, ATMService


class Command(BaseCommand):
    help = 'Reads data from the ATM API and populates the db'

    def handle(self, *args, **options):
        r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')
        data = r.json()['data']
        atm_list = data[0]['Brand'][0]['ATM']

        # First, delete any existing entries in the database
        ATM.objects.delete_all()
        ATMService.objects.delete_all()

        # Populate the ATM services with all the possible services
        populate_atm_services()

        for i, atm_data in enumerate(atm_list):
            atm = ATM()
            atm.atmid = atm_data['Identification']
            service_str = atm_data['ATMServices'][0]
            service = ATMService.objects.get(name=service_str)
            atm.save()
            atm.atm_services.add(service)
            self.stdout.write(atm_data['Identification'])
            if i > 10:
                break

        self.stdout.write(self.style.SUCCESS('Successfully updated database.'))

def populate_atm_services():
    services = ['PINUnblock', 'Balance']
    for service in services:
            ATMService.objects.create(name=service)



