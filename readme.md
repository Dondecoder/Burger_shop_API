# Name

## Burger_shop_API

## Installation

* Flask

* Flask-JWT

* Flask-RESTful

* Flask-SQLAlchemy 

## Description

This is a server-side REST API which allows you to create, read, update and delete data. Within this repo there are many versions of this API project. 

Version 1

* This version makes use of creating an internal database inorder to post, delete, update or retrieve items from it. The internal DB is a burgers list and as we make use of the filter function to map the list and make changes. We also use this version to create endpoint for each the resource

Version 2 

* This version improves on version 1 by introducting Sqlite3 database and with this version we are able to use this database to store information rather than creating an internal database. 

* This version introduces the use of SQL queries being use to create the table, inserting items, deleting items as well as updating items

* It uses a connection variable to connect the DB to the app.py file and generates a "data.db" file as well that creates the table

Version 3

* This is the primary version that is in this Repo. It makes use of SQLAlchemy and reduces the amount of code needed to create tables or connect to app.py

* This version also seperates the code and makes use of models and resources folder and seperates app.py into resources and model

* This version allows us to delete the creates_tables.py and create a table within the burgers.py in the models folder. 

* This was also deployed to Heroku as well. 
