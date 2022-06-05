from django.contrib import admin
from .models import Ticket, TicketResponse


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_content', 'tracking_code', 'status', 'is_open']
    list_filter = ['created_at', 'status']
    search_fields = ('tracking_code', 'title')

    def sub_content(self, obj):
        return f"{obj.content[:30]}"
    sub_content.short_description = 'content'


@admin.register(TicketResponse)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['sub_content', 'created_at']
    list_filter = ['created_at']

    def sub_content(self, obj):
        return f"{obj.content[:30]}"
    sub_content.short_description = 'content'
