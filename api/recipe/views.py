from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer, IngredientSerializer
from .models import Recipe, Ingredient
from django.http import JsonResponse
import json
from rest_framework.pagination import PageNumberPagination



class RecipeListViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
            return Recipe.objects.all()


class IngredientListViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()






def MyFridge(request):


    if not 'ingredients' in request.GET:
        data = []
        for rec in Recipe.objects.all():
            data.append(RecipeSerializer(rec).data)

        return JsonResponse(data, safe = False)
        

    query = request.GET.get('ingredients').split(",")
    query = list(dict.fromkeys(query))
    
    if 'salt' in query:
        query.remove('salt')

    if 'sugar' in query:
        query.remove('sugar')

    if('water') in query:
        query.remove('water')
    
    ingredient_list = Ingredient.objects.none()

    #All relevent ingredients in ingredient_list
    for item in query:
    
        if Ingredient.objects.filter(name = item).exists():
                
            temp = Ingredient.objects.filter(name = item)
            ingredient_list = ingredient_list.union(temp).distinct()
                
        
    #All possible (atleast 1 ingredient) in recipe_list
    recipe_list = Recipe.objects.none()

    for ingredient in ingredient_list:

        recipes = ingredient.recipes.all()
        recipe_list = recipe_list.union(recipes).distinct()
            
        
    relevant_recipe_id = []


    #Finding relevant recipes
        
    for recipe in recipe_list:
            
        total_ing = recipe.ingredients.count()
        matched_ing = 0
        recipe_ingredients = recipe.ingredients.all()

        for available_ing in query:
            
            if recipe_ingredients.filter(name__icontains = available_ing).exists():
                matched_ing+=1

        percentage_match = matched_ing/total_ing
            
        if percentage_match >= 0.8 or total_ing - matched_ing <=3 :
            relevant_recipe_id.append({'recipe_id' : recipe.id, 'percentage_match' : percentage_match})


        sorted(relevant_recipe_id, key= lambda i : i['percentage_match'])


    data = []
    
    for num in relevant_recipe_id:
        rec = Recipe.objects.get(id = num['recipe_id'])
        data.append(RecipeSerializer(rec).data)

    return JsonResponse(data, safe = False)

        