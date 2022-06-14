from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm
)
import re

User = get_user_model()


def validate_email(email):
    if re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        return True
    return False


def validate_phone(number):
    k = 0
    if re.match(r'^09\d{9}$' , number):
        k = 1
    if re.match(r'^\+98\d{10}$' , number):
        k = 1
    if re.match(r'^0098\d{10}$' , number) :
        k = 1

    if k == 1:
        return True
    return False


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email', 'id': 'email', 'class': 'form-control back'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'password', 'class': 'form-control'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is not None and password:
            self.user_cache = User.objects.filter(username=username).first()
            if not self.user_cache:
                self.user_cache = User.objects.filter(email=username).first()
            if self.user_cache is None:
                self.add_error('username', 'ایمیل یا نام کاربری اشتباه است!')
            else:
                self.confirm_login_allowed(self.user_cache)
                if self.user_cache.check_password(password):
                    return self.cleaned_data
                else:
                    self.add_error('password', 'رمز وارد شده اشتباه است!')
                    if not self.user_cache.is_active:
                        self.add_error('password', 'حساب کاربری شما فعال نیست!')
        return self.cleaned_data


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'username', 'id': 'username', 'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email', 'class': 'form-control'})
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'phone_number', 'id': 'phone_number', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'password1', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm-password', 'id': 'password2', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if validate_email(email):
            return email
        raise forms.ValidationError("ایمیل وارد شده اشتباه است.")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if validate_phone(phone_number):
            return phone_number
        raise forms.ValidationError("شماره تلفن صحیح نیست!")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور ها مغایرت دارند!")
        return password2

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'کاربری با این ایمیل از قبل موجود است !')
        else:
            if User.objects.filter(username=username).exists():
                self.add_error('username', 'کاربری با این نام کاربری از قبل موجود است !')

        return self.cleaned_data


class SetNewResetPasswordForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetNewResetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password1', 'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password2', 'class': 'form-control'})
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if password1 and password2:
            if password1 != password2:
                raise ValidationError("رمز های عبور مغایرت دارند!")
        return password2

    def save(self, commit=True):
        password = self.cleaned_data['new_password1']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class ChangePasswordForm(SetNewResetPasswordForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'pass-old', 'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("رمز عبور قبلی اشتباه است !")
        return old_password

    def clean(self):
        old_pass = self.cleaned_data.get('old_password')
        new_pass = self.cleaned_data.get('new_password2')
        if new_pass == old_pass:
            self.add_error('new_password2', 'رمز عبور جدید نباید با رمز قبلی برابر باشد!')
        return self.cleaned_data


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email', 'class': 'form-control'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            return email
        raise forms.ValidationError("ایمیل وارد شده اشتباه است!")


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True
        self.fields['username'].disabled = True

    class Meta:
        model = User
        fields = ('profile_image', 'username', 'email', 'first_name', 'last_name', 'phone_number')
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
                   'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstname'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastname'}),
                   'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'})
                   }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if validate_email(email):
            check_email_exist = User.objects.filter(email=email).exclude(email=self.user.email).exists()
            if check_email_exist:
                raise forms.ValidationError("این ایمیل از قبل استفاده شده است !ایمیل دیگری وارد کنید.")
            return email
        raise forms.ValidationError("ایمیل نامعتبر است !")
