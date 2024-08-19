from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["subject", "service", "message", "sender", "cc_myself"]
