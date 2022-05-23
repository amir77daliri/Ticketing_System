from django.shortcuts import render
from .forms import ContactUsForm
from django.contrib.auth.decorators import login_required


@login_required()
def contact_us(request):
    form = ContactUsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

    context = {
        'form': form
    }
    return render(request, 'ContactUs/contact-us.html', context)
