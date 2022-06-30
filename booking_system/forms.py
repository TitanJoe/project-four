from django import forms
from django.forms.widgets import DateTimeInput
from .models import booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['name', 'number_of_people', 'time_and_date']
        widgets = {
            'time_and_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
