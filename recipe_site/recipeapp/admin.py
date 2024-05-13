from django.contrib import admin
from .models import Recipe, Category, RecipeCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'preparation_time')
    search_fields = ('title', 'description', 'ingredients')
    list_filter = ('categories', 'author')

    def author_name(self, obj):
        return obj.author.username
    author_name.short_description = 'Автор'

class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('recipe_title', 'category_name', 'additional_info')
    search_fields = ('recipe__title', 'category__name')

    def recipe_title(self, obj):
        return obj.recipe.title
    recipe_title.short_description = 'Рецепт'

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Категория'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)