from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer, IngredientSerializer
from .models import Recipe, Ingredient
from django.http import JsonResponse
import json
from functools import reduce
import operator
from django.db.models import Q

class RecipeListViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    
    def get_queryset(self):

        if not 'ingredients' in self.request.GET:
            return Recipe.objects.filter(id__lte = 100)
            
        query = self.request.GET.get('ingredients').split(",")
        query = list(dict.fromkeys(query))
        
        if 'salt' in query:
            query.remove('salt')
        if 'sugar' in query:
            query.remove('sugar')
        if 'water' in query:
            query.remove('water')
    
        ingredient_list = Ingredient.objects.filter(name__in = query)
        recipe_list = Recipe.objects.filter(ingredients__in = ingredient_list)
        relevant_recipe_id = []

        if 'search' in self.request.GET:
            query = self.request.GET.get('search')
            clean_query = [x.strip() for x in query.split(',')]

            recipe_list =  recipe_list.filter(reduce(operator.and_, (Q(directions__icontains = x) for x in clean_query)))

        #Finding relevant recipes
        for recipe in recipe_list:
            
            if len(relevant_recipe_id) == 20:
                break
            total_ing = recipe.ingredients.count()
            matched_ing = 0
            recipe_ingredients = recipe.ingredients.all()

            for available_ing in query:
                
                if recipe_ingredients.filter(name__icontains = available_ing).exists():
                    matched_ing+=1

            percentage_match = matched_ing/total_ing
                
            if percentage_match >= 0.8 or total_ing - matched_ing <=2:
                relevant_recipe_id.append(recipe.id)

        recipes_final = Recipe.objects.filter(id__in = relevant_recipe_id)
        return recipes_final



            

class IngredientListViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


