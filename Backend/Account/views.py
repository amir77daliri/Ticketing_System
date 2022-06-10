from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import (
    views as auth_views,
    update_session_auth_hash
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    LoginForm,
    SignUpForm,
    MyPasswordResetForm,
    SetNewResetPasswordForm,
    ChangePasswordForm,
    ProfileUpdateForm
)


User = get_user_model()


def home(request):
    return render(request, 'Account/index.html', {})


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Account/login.html'


class Logout(LoginRequiredMixin, auth_views.LogoutView):
    pass


class Register(CreateView):
    form_class = SignUpForm
    template_name = 'Account/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        use_https = self.request.is_secure()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی حساب کاربری'
        message = render_to_string('Account/active_account_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            "protocol": "https" if use_https else "http"
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(self.request, 'Account/email-sent.html', {'email': form.cleaned_data.get('email')})


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
        return render(request, 'Account/activate-account-success.html', {})
    else:
        return HttpResponse('لینک فعالسازی منقضی شده است. مجددا اقدام کنید.')


class MyPasswordReset(auth_views.PasswordResetView):
    email_template_name = "Account/password_reset_email.html"
    form_class = MyPasswordResetForm
    template_name = 'Account/email-sent-pass.html'
    success_url = reverse_lazy('account:password_reset_done')


class MyPasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'Account/password_reset_done.html'


class MyPasswordResetConfirm(auth_views.PasswordResetConfirmView):
    form_class = SetNewResetPasswordForm
    template_name = 'Account/password-reset-confirm.html'
    success_url = reverse_lazy('account:login')


@login_required()
def change_password(request):
    form = ChangePasswordForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('ticket:user-profile')
    context = {
        'form': form
    }
    return render(request, 'Account/change-password.html', context)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'Account/profile.html'
    success_url = reverse_lazy('account:profile-info')

    def get_object(self, **kwargs):
        user = get_object_or_404(User, pk=self.request.user.id)
        return user

    def get_form_kwargs(self):
        kwargs = super(ProfileUpdate, self).get_form_kwargs()
        kwargs.update(
            {'user': self.request.user}
        )
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        print(form.cleaned_data.get('profile_image'))
        self.object = form.save()
        return super().form_valid(form)

