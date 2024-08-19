import after_response
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BookingForm
from .models import Promotion
from .tasks import send_booking_us_email


def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking form data to the database
            booking = form.save()

            # Prepare email sending
            recipients = ["idolls758@gmail.com"]
            if booking.cc_myself:
                recipients.append(booking.sender)
            booking_message = f"{booking.service.name}\n\n{booking.message}"
            # Send email asynchronously
            send_booking_us_email.after_response(
                booking.subject, booking_message, booking.sender, recipients
            )

            messages.success(request, "Thank you for your message.")
            return redirect("/") 
    else:
        form = BookingForm()

    return render(request, "promotions/booking.html", {"form": form})


class PromotionCreateView(CreateView):
    model = Promotion
    fields = ["title", "description", "image", "start_date", "end_date"]


class PromotionDetailView(DetailView):
    model = Promotion


class PromotionListView(ListView):
    model = Promotion


class PromotionUpdateView(UpdateView):
    model = Promotion
    fields = ["title", "description", "image", "start_date", "end_date"]
