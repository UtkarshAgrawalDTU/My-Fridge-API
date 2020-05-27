from django.contrib import admin
from django.urls import path
from rest_framework import routers
from recipe.views import RecipeListViewSet, IngredientListViewSet
router = routers.DefaultRouter()

router.register('recipes', RecipeListViewSet, 'Recipe')
router.register('ingredients', IngredientListViewSet, 'Ingredient')


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
