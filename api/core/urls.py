from django.contrib import admin
from django.urls import path
from rest_framework import routers
from recipe.views import RecipeListViewSet, IngredientListViewSet, MyFridge

router = routers.DefaultRouter()

router.register('recipe', RecipeListViewSet, 'Recipe')
router.register('ingredient', IngredientListViewSet, 'Ingredient')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfridge/', MyFridge),
]

urlpatterns += router.urls
