# Teleka Sacco Manger version 2.0: Django

This is a project  built on SAAS Python Django Framework to help manage small Savings And Credit Coperatives handle thier records keeping on the go without difficulty

## Login Page

<img width="652" alt="Login" src="https://user-images.githubusercontent.com/36954843/195980591-7eed3936-0b83-4030-8cd8-03a8e3f80947.png">

## Register Page

<img width="1267" alt="Register" src="https://user-images.githubusercontent.com/36954843/195980624-b59660b7-22d6-4957-9adf-115a6668c5f8.png">

## Dashbaord

<img width="642" alt="Dashboard" src="https://user-images.githubusercontent.com/36954843/195980658-44489193-0223-4d3f-8f4a-c4e9acd83e3d.png">

## Warnings

Please be sure to read the following instructions and considerations before running this code on your local workstation, shared systems, or production environments.


## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).


2. Fork this repo and clone your fork:

    `git clone https://github.com/alvienzo720/Teleka_V2`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Create a development database:

    `./manage.py migrate`

5. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.

