from django.core.management.base import BaseCommand, CommandError
import requests
from atms.models import ATM


class Command(BaseCommand):
    help = 'Reads data from the ATM API and populates the db'

    def handle(self, *args, **options):
        r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')
        data = r.json()['data']
        atm_list = data[0]['Brand'][0]['ATM']

        # First, delete any existing entries in the database
        ATM.objects.delete_all()

        for atm_data in atm_list:
            atm = ATM()
            atm.atmid = atm_data['Identification']
            atm.save()
            self.stdout.write(atm_data['Identification'])

        self.stdout.write(self.style.SUCCESS('Successfully updated database.'))