from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import requests
from atms.models import ATM, ATMService, Accessibility


class Command(BaseCommand):
    help = 'Reads data from the ATM API and populates the db'

    def handle(self, *args, **options):
        r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')
        data = r.json()['data']
        atm_list = data[0]['Brand'][0]['ATM']

        # First, delete any existing entries in the database
        ATM.objects.delete_all()
        ATMService.objects.delete_all()
        Accessibility.objects.delete_all()

        # Populate the ATM services with all possible services
        populate_atm_services()

        # Populate Accessibility with all possible options
        populate_accessibility_options()

        for i, atm_data in enumerate(atm_list):
            atm = ATM.objects.create(atmid=atm_data['Identification'])
            for j in range(len(atm_data['Accessibility'])):
                accessibility_str = atm_data['Accessibility'][j]
                self.stdout.write(f'{accessibility_str} is the string')
                accessibility = Accessibility.objects.get(name=accessibility_str)
                atm.accessibility.add(accessibility)
            atm.save()
            for j in range(len(atm_data['ATMServices'])):
                service_str = atm_data['ATMServices'][j]
                service = ATMService.objects.get(name=service_str)
                atm.atm_services.add(service)
            self.stdout.write(atm_data['Identification'])
            atm.save()
            if i > 10:
                break

        self.stdout.write(self.style.SUCCESS('Successfully updated database.'))


def populate_atm_services():
    services = [
        'PINUnblock',
        'Balance',
        'BillPayments',
        'CashWithdrawal',
        'FastCash',
        'MobilePhoneTopUp',
        'PINChange',
        'MiniStatement'
    ]
    for service in services:
        ATMService.objects.create(name=service)

def populate_accessibility_options():
    options = [
        'AudioCashMachine',
        'WheelchairAccess',
    ]
    for option in options:
        Accessibility.objects.create(name=option)
