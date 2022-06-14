from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('title', 'message')
        widgets = {'title': forms.TextInput(attrs={'type': 'text', 'placeholder': 'title', 'id': 'title', 'class': "form-control"}),
                   'message': forms.Textarea(attrs={'placeholder': 'Leave a comment here', 'id': 'message', 'class': 'form-control'})
                   }
