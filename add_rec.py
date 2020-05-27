#Script to add recipies from json file to database.

import json
from recipe.models import Recipe, Ingredient
from add_ing import remove, removespace

def create_rec_obj(r):
    name = r["Recipe Name"]
    img_url = r["Recipe Photo"]
    author = r["Author"] 
    prepare_time = r["Prepare Time"] 
    cook_time = r["Cook Time"] 
    total_time = r["Total Time"] 
    directions = r["Directions"] 
    ingredients_list = r["Ingredients"]
    rec = Recipe(name = name, img_url = img_url, author = author, prepare_time = prepare_time, cook_time = cook_time, total_time = total_time, directions = directions, ingredients_list = ingredients_list)
    return rec
    

def ing_label(r):
    ingredient = []
    ing = r['Ingredients'].split(",")
    for item in ing:
        ingredient.append(str(item))
    ingredient = remove(ingredient)
    ingredient = removespace(ingredient)
    return ingredient


with open('recipes.json') as f:
    recipes_json = json.load(f)


for r in recipes_json:
    obj = create_rec_obj(r)
    obj.save()
    ing_labels = ing_label(r)
    for label in ing_labels:
        Q = Ingredient.objects.get(name = label)
        obj.ingredients.add(Q)
    
