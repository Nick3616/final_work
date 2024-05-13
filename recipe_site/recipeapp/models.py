from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preparation_steps = models.TextField(verbose_name="Шаги приготовления")
    preparation_time = models.IntegerField(verbose_name="Время приготовления (минуты)")
    image = models.ImageField(upload_to='recipes/', verbose_name="Изображение", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    ingredients = models.TextField(verbose_name="Ингредиенты", null=True, blank=True)
    categories = models.ManyToManyField(Category, through='RecipeCategory', verbose_name="Категории")

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        
    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    additional_info = models.CharField(max_length=255, verbose_name="Дополнительная информация", null=True, blank=True)

    class Meta:
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категории рецептов'
        
    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"
