from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminAccessMixin
from .models import Ticket, TicketResponse
from django.urls import reverse_lazy
from .forms import SignTicketForm, TicketResponseForm


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


@require_POST
def show_ticket_content(request):
    ticket_id = request.POST.get('id')
    try:
        ticket = Ticket.objects.get(id=ticket_id)
        data = {
            'title': ticket.title,
            'status': ticket.status,
            'slug': ticket.slug,
            'content': ticket.content,
        }
        return JsonResponse({'data': data})
    except:
        return JsonResponse({'error': 'not found'})


class TicketDetail(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'Ticket/ticket-detail.html'
    context_object_name = 'ticket'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        self.ticket = get_object_or_404(Ticket, slug=slug)
        return self.ticket

    def get_context_data(self, **kwargs):
        context = super(TicketDetail, self).get_context_data(**kwargs)
        context['responses'] = self.ticket.responses.all()
        context['form'] = TicketResponseForm
        return context


class SignTicket(LoginRequiredMixin, CreateView):
    form_class = SignTicketForm
    template_name = 'Ticket/sign-ticket.html'

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.user = self.request.user
        ticket.save()
        return redirect(reverse_lazy('ticket:user-profile'))
