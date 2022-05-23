from django.urls import path
from .views import contact_us

app_name = 'Contact'
urlpatterns = [
    path('', contact_us, name='contact-us'),
]
