# LittleLemon Restaurant Application

Welcome to the LittleLemon Restaurant Application! This project is a restaurant management system that allows users to book tables, view the menu, and enjoy a delightful dining experience. The application is backed by Django and utilizes Djoser for user authentication.

## Table of Contents
- [LittleLemon Restaurant Application](#littlelemon-restaurant-application)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Setting up the Database](#setting-up-the-database)
    - [Run the application](#run-the-application)
  - [Authentication](#authentication)
    - [API Endpoints](#api-endpoints)
    - [User Login](#user-login)
    - [Obtaining an Authentication Token](#obtaining-an-authentication-token)
  - [Now you are all set to use the LittleLemon Restaurant Application! Happy dining!](#now-you-are-all-set-to-use-the-littlelemon-restaurant-application-happy-dining)
  - [Booking a Table](#booking-a-table)
  - [Viewing the Menu](#viewing-the-menu)

## Getting Started

### Installation


1. Clone the repository to your local machine:

```bash
git clone https://github.com/moti9/LittleLemonWebApplication.git
cd LittleLemonWebApplication.git
```
2. Activate the virtual environment
```bash
pipenv shell
```
3. Install the dependencies
```bash
pipenv sync
```

### Setting up the Database

- Before running the application, you need to set up the database. By default, this project uses SQLite as the database, but you can configure it to use other databases supported by Django.

4. Setup MySQL
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'PASSWORD',
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
**OR, Create a `.env` file in the root folder**
```bash
# .env
DATABASE = YOUR_MYSQL_DATABASE_NAME
USER     = YOUR_USERNAME             # default is root
PASSWORD = YOUR_MYSQL_PASSWORD
HOST     = localhost                 # or 127.0.0.1
PORT     = 3306
```

5. Make migrations

```bash
python manage.py makemigrations
```

6. Migrate

```bash
python manage.py migrate
```
### Run the application
7. Run the app
- Start the development server to run the LittleLemon Restaurant Application:
```bash
python manage.py runserver
```

**The application will be accessible at http://127.0.0.1:8000/ .**


## Authentication
<p>
The application uses Djoser for user authentication. Below are the API endpoints provided by Djoser for 
</p>

### API Endpoints

- User Registration: /auth/users/ (POST)
- User Login: /auth/token/login/ (POST)
- User Logout: /auth/token/logout/ (POST)
- User Password Change: /auth/users/set_password/ (POST)
- User Password Reset: /auth/users/reset_password/ (POST)
- User Password Reset Confirmation: /auth/users/reset_password_confirm/ (POST)
- User Activation Email Resend: /auth/users/resend_activation/ (POST)
- User Activation: /auth/users/activation/ (POST)
- User Details: /auth/users/me/ (GET)


**Many more...**


<p>User Registration - To register a new user, make a POST request to /auth/users/ with the following JSON data:</p>

```bash
{
  "email": "example@example.com",
  "username": "example_user",
  "password": "your_password"
}
```

### User Login


To log in as a user, make a POST request to /auth/token/login/ with the following JSON data:

```bash
{
  "email": "example@example.com",
  "password": "your_password"
}
```

### Obtaining an Authentication Token


After a successful login, the response will contain an authentication token that you need to include in the headers of subsequent requests to authenticate the user:

```bash
{
  "auth_token": "your_auth_token_here"
}
```

**Include the token in the header as follows:**

```bash 
Authorization: Token your_auth_token_here
```

## Now you are all set to use the LittleLemon Restaurant Application! Happy dining!

## Booking a Table

TODO: Add instructions for booking a table.

## Viewing the Menu

TODO: Add instructions for viewing the menu.
