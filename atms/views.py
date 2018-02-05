from django.shortcuts import render
import requests
import json

def list(request):
    """
    Retuns ATM info
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v1.2/atms')

    # walk through the ATM objects and extract lat and long to dict
    data = r.json()['data']
    locations = []
    for atm in data:
        latitude = atm['GeographicLocation']['Latitude']
        longitude = atm['GeographicLocation']['Longitude']
        locations.append((latitude, longitude))


    return render(request, 'index.html', {'locations':locations})
