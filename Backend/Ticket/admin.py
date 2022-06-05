from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_content', 'tracking_code', 'status', 'is_open']
    list_filter = ['created_at', 'status']
    search_fields = ('tracking_code', 'title')

    def sub_content(self, obj):
        return f"{obj.content[:30]}"
    sub_content.short_description = 'content'
