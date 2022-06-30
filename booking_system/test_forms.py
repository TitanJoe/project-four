from django.test import TestCase
from .forms import BookingForm

class TestBookingForm(TestCase):

    def test_booking_name_is_required(self):
        form = BookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_booking_number_of_people_is_required(self):
        form = BookingForm({'number_of_people': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_people', form.errors.keys())
        self.assertEqual(form.errors['number_of_people'][0], 'This field is required.')

    def test_booking_time_and_date_is_required(self):
        form = BookingForm({'time_and_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time_and_date', form.errors.keys())
        self.assertEqual(form.errors['time_and_date'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['name', 'number_of_people', 'time_and_date'])