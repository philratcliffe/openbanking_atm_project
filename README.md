# Open Banking ATMs

## Overview
An app to exercise an Open Banking API. It gets ATM data from
a bank and presents it as locations on a map and in formatted JSON.

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

* Under Django settings, set the required environment variables.

* Create a Django server configuration for running the project.
 
* Under the Django server configuration set the required environment variables.

## Notes if running under Docker

### .env file
Set up the necessary environment variables in this file. Below is
an example of a .env file.

```bash
# Local file only; keep this out of source control.
DJANGO_SECRET_KEY=changethisforproduction
GOOGLE_API_KEY=yourGoogleAPIKeyHere

```

### running migrate
To run database migrations use the command below.

```bash 
$ docker-compose run web python manage.py migrate --settings openbanking_atm_project.settings.local
```

###
To run the application use the command below.

```bash 
$ docker-compose up
```

