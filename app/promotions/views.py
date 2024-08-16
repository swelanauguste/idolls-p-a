import after_response
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ContactForm
from .models import Promotion
from .tasks import send_contact_us_email


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact form data to the database
            contact = form.save()

            # Prepare email sending
            recipients = ["idolls758@gmail.com"]
            if contact.cc_myself:
                recipients.append(contact.sender)
            contact_message = f"{contact.service.name}\n\n{contact.message}"
            # Send email asynchronously
            send_contact_us_email.after_response(
                contact.subject, contact_message, contact.sender, recipients
            )

            messages.success(request, "Thank you for your message.")
            return redirect("/") 
    else:
        form = ContactForm()

    return render(request, "promotions/contact.html", {"form": form})


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
