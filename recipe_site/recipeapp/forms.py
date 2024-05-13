from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'preparation_time', 'ingredients', 'categories', 'image']
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Обязательное поле.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)