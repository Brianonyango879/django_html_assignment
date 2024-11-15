### Create the Django Project Folder
using git bash create a django project folder:
    cd desktop
    cd PycharmProjects
    mkdir Django Assignment 
### Open the project folder using pycharm
Setting a Django Project
    1. start a new Django Project
    django-admin startproject portfolio_site
    cd portfolio_site
    2. create a new app
    python manage.py startapp template
    3. register the app in portfolio_site/settings.py
    In Installed apps add 'portfolio',
### create the contact model
    import: 'from django.db import models
### run migrations
-This create the contact table in the database
    python manage.y makemigrations
    python manage.py migrate
### Making sure the database is functioning
in the file section click file
### create the contact form
    imports: 'from django import forms'
             'from .models import Contact'
### set up the contact view and template
-In the portfolio/views.py create a view to handle the contact form
        imports: 'from django.shortcuts import render, redirect'
                 'from .forms import ContactForm'
### Add Urls in portfolio/urls.py
    imports: 'from django.urls import path'
             'from . import views'
### Create the contact form template (portfolio/templates/portfolio/contact.html)
    <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
### Create a success page template 
(portfolio/templates/portfolio/contact_success.html)
### Create a template directory
create a index.html
### add a css folder
create a style.css style sheet inside it
### Run the server
In the terminal you run the server by:
        python manage.py runserver
Run the https link: http://127.0.0.1:8000/
