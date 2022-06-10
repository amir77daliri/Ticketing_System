from django.urls import path
from .views import (
    Login,
    Logout,
    Register,
    activate,
    MyPasswordReset,
    MyPasswordResetDone,
    MyPasswordResetConfirm,
    ProfileUpdate,
    change_password
)

app_name = 'account'
urlpatterns = [
    path('info/', ProfileUpdate.as_view(), name='profile-info'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('active/<uidb64>/<token>/', activate, name='activate'),
    path('password_change/', change_password, name='password_change'),
    path('password_reset/', MyPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', MyPasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirm.as_view(), name='password_reset_confirm'),
]
