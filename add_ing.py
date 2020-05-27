#Script to add ingredients from json file to database


import json
import re 

def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    list = [item.replace('/', '') for item in list]
    list = [item.replace('(', '') for item in list]
    list = [item.replace(')', '') for item in list] 
    list = [item.replace(':', '') for item in list]
    list = [item.replace('.', '') for item in list]
    list = [item.replace('-', '') for item in list]
    list = [item.replace("'", '') for item in list]
    list = [item.replace('\x99', '') for item in list]
    list = [item.replace('tablespoons', '') for item in list]
    list = [item.replace('ounces', '') for item in list]
    list = [item.replace('pounds', '') for item in list]
    list = [item.replace('pound', '') for item in list]
    list = [item.replace('and', '') for item in list]
    list = [item.replace('cups', '') for item in list]
    list = [item.replace('ounce', '') for item in list]
    list = [item.replace('cup', '') for item in list]
    list = [item.replace('tablespoon', '') for item in list]
    return list

def removespace(list):
    newlist = []
    for item in list:
        newlist.append(" ".join(item.split()).lower())
    return newlist


with open('recipes.json') as f:
    recipes_json = json.load(f)

ingredient = []

for recipe in recipes_json:
        ing = recipe['Ingredients'].split(",")
        for item in ing:
            ingredient.append(str(item))

ingredient = remove(ingredient)
ingredient = removespace(ingredient)

while("" in ingredient) : 
    ingredient.remove("") 

finallist = list(dict.fromkeys(ingredient))
