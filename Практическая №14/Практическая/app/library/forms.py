from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import CartItem
from library.models import CartItem

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
    
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if not password:
            raise forms.ValidationError(('Пожалуйста, введите пароль'))
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError(('Пожалуйста, введите логин'))
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(('Пожалуйста, введите электронную почту'))
        return email
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity',)