# What's In My Fridge? REST API
> What's In My Fridge? is a REST API which suggests users various recipes based on the ingredients selected. Check it out here: [What's In My Fridge? REST API](https://myfridgeapi.herokuapp.com)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Status](#status)
* [Authors](#authors)
* [Inspiration](#inspiration)


## General info
The project consists of a database consisting of 10,000+ unique recipies and 700+ different ingredients to choose from. Users can enter the ingredients available to them in their home/fridge, and the API will suggest possible recipes which can be prepared from those ingredients!


## Technologies
* Django - Python Web Framework
* Django Rest Framework - A Django Framework to create REST API's
* Heroku - Used for Deployment
* Gunicorn - Application Server
* PostgreSQL - Database Management System


## Endpoints
List of endpoints to fetch data
* List pf Recipes : "https://myfridgeapi.herokuapp.com/recipes"
* Unique Recipe from id : "https://myfridgeapi.herokuapp.com/recipes/id"
* List of Ingredients : "https://myfridgeapi.herokuapp.com/ingredients"
* Unique Ingredient from id : "https://myfridgeapi.herokuapp.com/ingredients/<id>"
* Suggested Recipes : "https://myfridgeapi.herokuapp.com/myfridge/?ingredients=<ingredient_list seperated by commas>&search=<your search query>"


## Status
Project is __finished__

## Authors
* Utkarsh Agrawal - [UtkarshAgrawalDTU](https://github.com/UtkarshAgrawalDTU)
