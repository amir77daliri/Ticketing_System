from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'message', 'status', 'created_at']
    list_filter = ['status']
    ordering = ['created_at']

