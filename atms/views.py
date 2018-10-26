from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.list import ListView
import requests
import json

from .models import ATM


class HomeView(TemplateView):
    """Displays the home page"""
    template_name = "home.html"


class ATMListView(ListView):
    """List ATM data from the database"""
    template_name = "atms/local_list.html"
    queryset = ATM.objects.all()
    context_object_name = 'atm_list'


def map(request):
    """
    Displays ATM info on a map
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')

    # walk through the ATM objects and extract latitude and longitude
    data = r.json()['data']
    atm_list = data[0]['Brand'][0]['ATM']
    locations = []
    for atm in atm_list:
        latitude = atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Latitude']
        longitude = atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Longitude']
        locations.append((latitude, longitude))

    return render(request, 'map.html', {'locations': locations, 'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})


def list(request):
    """
    Displays ATM info in JSON format.
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')

    atm_json_pretty = json.dumps(r.json(), sort_keys=True, indent=4)

    return render(request, 'list.html', {'atm_json_pretty': atm_json_pretty})
