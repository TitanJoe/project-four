from django.shortcuts import render, redirect, get_object_or_404
from .models import booking
from .forms import BookingForm


def get_bookings_list(request):
    bookings = booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking_system/bookings_list.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_bookings_list')
    form = BookingForm()
    context = {
        'form' : form
    }
    return render(request, 'booking_system/add_booking.html', context)