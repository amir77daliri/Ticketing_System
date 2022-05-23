from django.urls import path
from .views import (
    Login,
    Logout,
    Register,
    activate,
)


app_name = 'account'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('active/<uidb64>/<token>/', activate, name='activate'),
]
