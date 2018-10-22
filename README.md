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
    
## Required environment variables
Before running the Django project, you will need to set the following environment variables:

* GOOGLE_API_KEY
* DJANGO_SECRET_KEY
    
## Notes for running in PyCharm
If you wish to run this under PyCharm, follow the instructions below.

* Under Django settings, set the required environment variables (see above)

* Under Django settings, set the required environment variable.

* Create a Django server configuration for running the project.
 
* Under the Django server configuration set the required environment variable.