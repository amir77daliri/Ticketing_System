from django.urls import path
from .views import (
	AdminProfile,
	UserProfile,
	show_ticket_content
)

app_name = 'ticket'
urlpatterns = [
	path('admin_profile/', AdminProfile.as_view(), name='admin-profile'),
	path('user_profile/', UserProfile.as_view(), name='user-profile'),
	path('get_ticket_content/', show_ticket_content, name='ticket_content'),
]

