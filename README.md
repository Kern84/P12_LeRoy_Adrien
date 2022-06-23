[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# Project 12

Epic Events wants to create a CRM (Customer Relationship Management) app that allow users to create and manage Users (if admin), Clients, Contracts, Events and Event-statuses.
We have to create the back-end app / API Rest using Django REST Framework.

## Technologies

- PYTHON

## Authors

Adrien LE ROY

## Configuration for program execution

The program was designed with Python 3.10.
Download the project file on GitHub : https://github.com/Kern84/P12_LeRoy_Adrien.git

Download and install PostgreSQL and pgAdmin4 on your computer.
Create a database with the settings of your choice.
Transpose your database configuration into the EpicEvents/settings.py file.

Enter the commend lines in your terminal.
Go to the project folder, install and activate the virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

Install the packages needed for the project to work:
```
pip install -r requirements.txt
```

Migrate the project models to the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create a superuser:
```
python3 manage.py createsuperuser
```
And follow the instructions.

Launch the server:
```
python3 manage.py runserver
```

The local adress of the site:
http://127.0.0.1:8000

Or:
You can now connect to django admin http://127.0.0.1:8000/admin with the superuser information.


Deactivate the virtual environment when you are done viewing the project:
```
deactivate
```

## Postman documentation

https://documenter.getpostman.com/view/19829460/UzBpMSWH
