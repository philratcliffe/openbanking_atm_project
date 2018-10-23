from django.test import TestCase
from .models import ATM


class ATMTestCase(TestCase):
    def setUp(self):
        ATM.objects.create(atmid='1')

    def test_get_object_from_id(self):
        atm = ATM.objects.get(atmid='1')
        self.assertTrue(atm, "There is no atm object created.")




