# Open Banking ATMs

## Overview
An app to exercise an Open Banking API. It gets data on ATMs from
a bank and presents ATM locations on a map, it also shows the ATM data in formatted JSON.

## Running the Django development server
The command to run the Django development server is shown below.
```bash
$python manage.py runserver --settings=openbanking_atm_project.settings.local
```

## Viewing the results 
#### The ATM map
The ATM map can be viewed at:
    http://localhost:8000/atms/map

#### The ATM data 
The ATM data can be viewed at:
    http://localhost:8000/atms/list
    
## Notes for running in PyCharm
If you wish to run this under PyCharm, follow the instructions below.

* Under Django settings, set DJANGO support enabled for the project.

* Under Django settings, set the DJANGO_SECRET_KEY environment variable.

* Create a Django server configuration for running the project.
 
* Under the Django server configuration set the DJANGO_SECRET_KEY environment variable.