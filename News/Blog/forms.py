from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class AddPageForm(forms.ModelForm):
    name = forms.CharField(label='Title',
                           widget=forms.TextInput(attrs={'placeholder': 'title', 'name': 'name', 'class': "form-control"}))
    image = forms.ImageField(label='Image', widget=forms.FileInput(
         attrs={'class': "form-control", 'name':'image','style': 'margin-top: 20px; margin-bottom: 20px;'}))
    text = forms.CharField(label='Text', widget=forms.Textarea(
         attrs={'placeholder': 'text', 'class': "form-control",'style': 'margin-bottom: 20px;', 'name':'text', 'cols': 60, 'row': 10}))

    class Meta:
        model = Post
        exclude = ('create_at', 'author', 'slug','id')


class RegisterUserForm(UserCreationForm):  # класс формы для регистрации
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'placeholder': 'name', 'class': "form-control"}))  # переопределение полей
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': "form-control"}))
    password1 = forms.CharField(label='Пороль', widget=forms.PasswordInput(
        attrs={'placeholder': 'password', 'class': "form-control"}))  # переопределение полей
    password2 = forms.CharField(label='Повтор пороля', widget=forms.PasswordInput(
        attrs={'placeholder': 'password repit', 'class': "form-control"}))  # переопределение полей

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreateProfileForm(forms.ModelForm):

    status = forms.CharField(label='Status',widget=forms.TextInput(attrs={'placeholder': 'Status', 'name': 'status', 'class': "form-control"}))
    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(attrs={'class': "form-control", 'name':'avatar','style': 'margin-top: 20px; margin-bottom: 20px;'}))
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.DateInput(attrs={'placeholder': 'Date of birth', 'name': 'date_of_birth', 'class': "form-control"}))
    about_me = forms.CharField(label='About_me', widget=forms.Textarea(attrs={'placeholder': 'About_me', 'class': "form-control",'style': 'margin-top: 20px; margin-bottom: 20px;', 'name':'text', 'cols': 60, 'row': 10}))
    class Meta:
        model = Profile
        fields = ['status', 'avatar', 'date_of_birth', 'about_me']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'placeholder': 'name', 'class': "form-control"}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': "form-control"}))
