from django.urls import path
from .views import (
	AdminProfile,
	UserProfile,
	show_ticket_content,
	TicketDetail,
	SignTicket,
)

app_name = 'ticket'
urlpatterns = [
	path('admin_profile/', AdminProfile.as_view(), name='admin-profile'),
	path('user_profile/', UserProfile.as_view(), name='user-profile'),
	path('get_ticket_content/', show_ticket_content, name='ticket_content'),
        path('sign-ticket/', SignTicket.as_view(), name='sign-ticket'),
	path('<slug:slug>/', TicketDetail.as_view(), name='ticket-detail'),
]

