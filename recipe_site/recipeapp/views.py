from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RecipeForm, RegistrationForm, LoginForm

def home(request):
    recipes = Recipe.objects.order_by('?')[:5]  # Получение 5 случайных рецептов
    return render(request, 'home.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request, pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.user != recipe.author:
            return HttpResponseForbidden()
    else:
        recipe = Recipe(author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'add_edit_recipe.html', {'form': form})

@login_required
def edit_recipe(request, pk=None):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author and not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'add_edit_recipe.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    error_message = None
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Неверное имя пользователя или пароль'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def logout(request):
    auth_logout(request)
    return redirect('home')

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'recipes': recipes})