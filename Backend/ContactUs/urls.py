from django.urls import path
from .views import contact_us, MessagesList, show_message_content


app_name = 'Contact'
urlpatterns = [
    path('', contact_us, name='contact-us'),
    path('messages-list/', MessagesList.as_view(), name='messages-list'),
    path('show-message-content/', show_message_content, name='message-content')
]
