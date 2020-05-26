if not 'ingredients' in self.request.GET:
        return Recipe.objects.all()
        
        query = self.request.GET.get('ingredients').split(",")
        query = list(dict.fromkeys(query))
        
        ingredient_list = Ingredient.objects.none()

        #All relevent ingredients in ingredient_list
        for item in query:
    
            if Ingredient.objects.filter(name__icontains = item).exists():
                
                temp = Ingredient.objects.filter(name__icontains = item)
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

                if recipe_ingredients.filter(name__icontains = available_ing).existsfr():
                    matched_ing+=1

            percentage_match = matched_ing/total_ing
            
            if percentage_match >= 0.8 or total_ing - matched_ing <=3 :
                relevant_recipe_id.append({'recipe_id' : recipe.id, 'percentage_match' : percentage_match})


        
        return relevant_recipe_id
