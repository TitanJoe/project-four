from django.db.models.fields import DateTimeField
from django.test import TestCase
from .models import booking


class TestViews(TestCase):
    
    def test_get_bookings_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_system/bookings_list.html')
    
    def test_get_add_booking_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_system/add_booking.html')

    def test_get_edit_booking_page(self):
        bookings = booking.objects.create(name='Test Booking', number_of_people=1, time_and_date=DateTimeField.auto_now)
        response = self.client.get(f'/edit/{bookings.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_system/edit_booking.html')
    
    def test_can_add_booking(self):
        response = self.client.post('/add', {'name': 'Test Added Booking', 'number_of_people': 1})
        self.assertRedirects(response, '/')

    def test_can_delete_booking(self):
        bookings = booking.objects.create(name='Test Booking', number_of_people=1, time_and_date=DateTimeField.auto_now)
        response = self.client.get(f'/delete/{bookings.id}')
        self.assertRedirects(response, '/')
        existing_bookings = booking.objects.filter(id=bookings.id)
        self.assertEqual(len(existing_bookings), 0)

