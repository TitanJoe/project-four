from django.shortcuts import render, redirect, get_object_or_404
from .models import booking


def get_bookings_list(request):
    bookings = booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking_system/bookings_list.html', context)
