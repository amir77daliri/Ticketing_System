from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
    views as auth_views,
    update_session_auth_hash
)
from .forms import (
    LoginForm,
)


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Account/login.html'


class Logout(LoginRequiredMixin, auth_views.LogoutView):
    pass