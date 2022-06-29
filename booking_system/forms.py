from django import forms
from .models import booking
from django.forms.widgets import DateTimeInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['name', 'number_of_people', 'time_and_date']
        widgets = {
            'time_and_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }