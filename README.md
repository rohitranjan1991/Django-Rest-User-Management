# Django Rest Project

This project is a very basic project to show the implementation of the rest standard apis for User Management. It includes the basic GET, PATCH, POST and DELETE apis for managing the user resource.

## Getting Started

### Prerequisites

The pre-requisites are:
```
 python: 3.x.x
 virtualenv -  for creating a local environment in which the project will run
 pip - the package installer for python

```
----------


### Installing

The installation process is as follows:

 - Change the terminal directory to the project directory
 - Create a virtual Environment

	Lets create a virtual environment to ensure that your global packages are not affected. To create a virtualenv execute the below command inside the project directory:
	```
	virtualenv -p python3 venv
	```
	The "-p" ensures that the virtualenv is created using the python version 3

 - Install Dependencies

	To install the dependent packages for this project run the following command:

	```
	pip install -r requirements.txt
	```

 - Database Setup

	This project for now is using a sqlite Database which is the default DB provided by Django Framework which is defined in the settings.py file as bellow

	```
	...

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}

	...
	```
	but if you want to point to MySQL database you'll have to change it to be something like this
	```
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': '<database>',
	        'USER': '<username>',
	        'PASSWORD': '<password>',
	        'HOST': '<host_ip>',
	        'PORT': '',
	    }
	}
	```

	Once you have settled in the database, run
	```
	python manage migrate
	```
	This will setup the tables required for the project based on the models


## Deployment

To run the server just follow the below steps

 - Activate the Virtual Environment

	> source venv/bin/activate

 - Start server

	> python manage.py runserver

	The server will start by default at port 8000 and will be accessible at http://localhost:8000

## Endpoints
The endpoints available are:

 - **POST**:
	Adds a new user

	 URL : `/userMgmt/user`
	 Body:
```
{
  "first_name": "Rohit",
  "last_name": "Ranjan",
  "email": "91.rohit@gmail.com",
  "phone_number": "+91-8050700005",
  "role": "regular"
}
```
 - **GET**:
	 Retrieves a user with {user_id} or if the {user_id} is not passed then it fetches all the users in the system

	 URL : `/userMgmt/user/{user_id}`
 - **PATCH**
 	  Updates the user detail

	  URL : `/userMgmt/user/{user_id}`
	 Body:
```
{
  "first_name": "Rohit1",
  "last_name": "Ranjan1",
  "role": "admin"
}
```
 - **DELETE**
	 Deletes the user resource

	 URL : `/userMgmt/user/{user_id}`

##Testing

- **Create a new user** :

    ```
    curl -X "POST" "http://localhost:8000/userMgmt/user" \
         -H 'Content-Type: application/json' \
         -d $'{
      "email": "91.rohit@gmail.com",
      "last_name": "Ranjan",
      "phone_number": "+91-8050700005",
      "first_name": "Rohit",
      "role": "regular"
    }'
    
    ```
- **Update an existing user** :

    ```
    curl -X "PATCH" "http://localhost:8000/userMgmt/user/1" \
         -H 'Content-Type: application/json' \
         -d $'{
      "first_name": "Rohit",
      "last_name": "Ranjan"
    }'

    ```
- **Retrive user** :

    ```
    ## Get All Users
    curl "http://localhost:8000/userMgmt/user" \
         -H 'Content-Type: application/json'

    
    ## Get user by ID
    curl "http://localhost:8000/userMgmt/user/1" \
         -H 'Content-Type: application/json'

    ```

- **Delete user** :
    
    ```
    curl -X "DELETE" "http://localhost:8000/userMgmt/user/1" \
         -H 'Content-Type: application/json' \
         -d $'{
      "email": "91.rohit@gmail.com",
      "last_name": "Ranjan",
      "phone_number": "+91-8050700005",
      "first_name": "Rohit",
      "role": "regular"
    }'

    ```
##Notes

 - The Debug setting is left to be True for the debugging purpose in the file `settings.py`
 
    `DEBUG=TRUE`

## Built With

* [Django](https://www.djangoproject.com/) - The python web framework used

## Authors

* **Rohit Ranjan**
