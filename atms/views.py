from django.shortcuts import render
import requests
import json

def list(request):
    """
    Retuns ATM info
    """

    r = requests.get('https://api.lloydsbank.com/open-banking/v1.2/atms')
    json_pretty = json.dumps(r.json(), sort_keys=True, indent=4)
    return render(request, 'index.html', {'atms_json':json_pretty})
