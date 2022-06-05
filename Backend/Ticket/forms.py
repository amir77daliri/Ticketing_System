from django import forms
from .models import Ticket


class SignTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'content')
        widgets = {'title': forms.TextInput(attrs={'type': 'text', 'placeholder': 'title', 'id': 'title', 'class': "form-control "}),
                   'content': forms.Textarea(attrs={'id': 'message', 'class': 'form-control fixText', 'style': 'height: 250px;'})
                   }

    def clean(self):
        title = self.cleaned_data.get('title')
        if title:
            title_length = len(title)
            if title_length > 200:
                self.add_error('title', 'حداکثر کاراکتر مجاز 200 می باشد!')
        return self.cleaned_data


class TicketResponseForm(forms.Form):
    response = forms.CharField(
        widget=forms.Textarea(attrs={'name': 'message', 'id': 'content', 'class': 'form-control', 'style': 'height: 250px;'})
    )
