from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm
)
import re

User = get_user_model()


def validate_email(email):
    if re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        return True
    return False


def validate_phone(number):
    k = 0
    if re.match(r'^09\d{9}$' , number):
        k = 1
    if re.match(r'^\+98\d{10}$' , number):
        k = 1
    if re.match(r'^0098\d{10}$' , number) :
        k = 1

    if k == 1:
        return True
    return False


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email', 'id': 'email', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'password', 'class': 'form-control'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is not None and password:
            self.user_cache = User.objects.filter(username=username).first()
            if not self.user_cache:
                self.user_cache = User.objects.filter(email=username).first()
            if self.user_cache is None:
                self.add_error('username', 'ایمیل یا نام کاربری اشتباه است!')
            else:
                self.confirm_login_allowed(self.user_cache)
                if self.user_cache.check_password(password):
                    return self.cleaned_data
                else:
                    self.add_error('password', 'رمز وارد شده اشتباه است!')
                    if not self.user_cache.is_active:
                        self.add_error('password', 'حساب کاربری شما فعال نیست!')
        return self.cleaned_data
