import after_response
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BookingForm
from .models import Banner, Service, Social, Value, WhyUs
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

            messages.success(
                request,
                "Thank you for reaching out to I-Dolls Promotional Agency! We’ve received your message and will get back to you shortly. We look forward to helping you elevate your next event!",
            )
            return redirect("/")
    else:
        form = BookingForm()
        socials = Social.objects.all()

    return render(request, "page/booking.html", {"form": form, "socials": socials})


def home_view(request):
    context = {
        "values": Value.objects.all(),
        "whys": WhyUs.objects.all(),
        "socials": Social.objects.all(),
        "banners": Banner.objects.all(),
    }
    return render(request, "page/home.html", context)


def services_view(request):
    context = {
        "services": Service.objects.filter(is_premium=False),
        "premium": Service.objects.filter(is_premium=True),
        "socials": Social.objects.all(),
    }
    return render(request, "page/services.html", context)


class ValueListView(ListView):
    model = Value
    extra_context = {
        "socials": Social.objects.all(),
    }
