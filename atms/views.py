from django.shortcuts import render
import requests
import json
from django.conf import settings


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
    Returns ATM info
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v2.2/atms')

    atm_json_pretty = json.dumps(r.json(), sort_keys=True, indent=4)

    return render(request, 'list.html', {'atm_json_pretty': atm_json_pretty})
