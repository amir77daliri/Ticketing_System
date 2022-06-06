from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminAccessMixin


class AdminProfile(LoginRequiredMixin, AdminAccessMixin, ListView):
    queryset = Ticket.objects.all()
    template_name = 'Ticket/admin-dashboard.html'
    context_object_name = 'tickets'
    paginate_by = 2


class UserProfile(LoginRequiredMixin, ListView):
    template_name = 'Ticket/user-dashboard.html'
    context_object_name = 'tickets'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        if request.user.is_admin:
            return redirect(reverse_lazy('ticket:admin-profile'))
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404("not found")
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

