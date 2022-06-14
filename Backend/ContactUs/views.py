from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ContactUsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Ticket.mixins import AdminAccessMixin
from .models import ContactUs


class MessagesList(LoginRequiredMixin, AdminAccessMixin, ListView):
    queryset = ContactUs.objects.all()
    template_name = 'ContactUs/admin-dashboard-messages.html'
    context_object_name = 'messages'
    paginate_by = 8


@login_required()
def contact_us(request):
    form = ContactUsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "پیغام شما با موفقیت ثبت شد.")

    context = {
        'form': form
    }
    return render(request, 'ContactUs/contact-us.html', context)


@require_POST
def show_message_content(request):
    message_id = request.POST.get('id')
    try:
        message = ContactUs.objects.get(id=message_id)
        message.status = 'd'
        message.save()
        data = {
            'title': message.title,
            'message': message.message,
        }
        return JsonResponse({'data': data})
    except:
        return JsonResponse({'error': 'not found'})
