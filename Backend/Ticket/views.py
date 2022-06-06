from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminAccessMixin


class AdminProfile(LoginRequiredMixin, AdminAccessMixin, ListView):
    queryset = Ticket.objects.all()
    template_name = 'Ticket/admin-dashboard.html'
    context_object_name = 'tickets'
    paginate_by = 2

