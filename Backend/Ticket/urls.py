from django.urls import path
from .views import (
	AdminProfile,
)

app_name = 'ticket'
urlpatterns = [
	path('admin_profile/', AdminProfile.as_view(), name='admin-profile'),
	path('user_profile/', UserProfile.as_view(), name='user-profile'),
]

