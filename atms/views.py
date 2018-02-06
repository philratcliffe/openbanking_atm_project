from django.shortcuts import render
import requests
import json

def map(request):
    """
    Displays ATM info on a map
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v1.2/atms')

    # walk through the ATM objects and extract latitude and longitude
    data = r.json()['data']
    locations = []
    for atm in data:
        latitude = atm['GeographicLocation']['Latitude']
        longitude = atm['GeographicLocation']['Longitude']
        locations.append((latitude, longitude))


    return render(request, 'map.html', {'locations':locations})

def list(request):
    """
    Returns ATM info
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v1.2/atms')
    atm_json_data = r.json()
    atm_json_pretty = json.dumps(r.json(), sort_keys=True, indent=4)

    return render(request, 'list.html', {'atm_json_pretty':atm_json_pretty})
