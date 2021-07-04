from django.utils import timezone

from django import forms
from .models import Inscription


class InscriptionForm(forms.ModelForm):
    def clean_date_created(self):
        data = self.cleaned_data['date_created']
        if data < timezone.now():
            data = timezone.now()
        return data

    def clean_cover(self):
        data = self.cleaned_data['cover']
        if data == "":
            data = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo90D-727qw6WMKpUCl0mpzBa5TLFqvsTfPg&usqp=CAU"
        return data

    class Meta:
        model = Inscription
        fields = ['title', 'desc', 'content', 'date_created', 'cover']
        labels = {'title': ('Title'), 'desc': ('Description'), 'date_created': ('Date Created'), 'cover': ('Cover picture')}
        help_texts = {'desc': ('Provide a brief description of note'), 'cover': ('Provide a link to an image')}

