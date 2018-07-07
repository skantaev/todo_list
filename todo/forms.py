from django.forms import ModelForm, TextInput

from .models import ListElement


class ListElementForm(ModelForm):

    class Meta:
        model = ListElement
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'text': '',
        }
