from django import forms

from .models import ShortUrl


class CreateShortURLForm(forms.ModelForm):
    original = forms.CharField(label='Original')

    class Meta:
        model = ShortUrl
        exclude = ('slug', '')