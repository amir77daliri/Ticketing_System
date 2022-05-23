from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    views as auth_views,
    update_session_auth_hash
)
from .forms import (
    LoginForm,
    SignUpForm,
)


User = get_user_model()


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Account/login.html'
    success_url = reverse_lazy('home')


def home(request):
    return render(request, 'Account/index.html', {})


class Logout(LoginRequiredMixin, auth_views.LogoutView):
    pass


class Register(CreateView):
    form_class = SignUpForm
    template_name = 'Account/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی حساب کاربری'
        message = render_to_string('Account/active_account_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(self.request, 'Account/confirm_email_send.html', {'email': form.cleaned_data.get('email')})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return render(request, 'Account/confirm_active_email_send.html', {})
    else:
        return HttpResponse('لینک فعالسازی منقضی شده است. مجددا اقدام کنید.')