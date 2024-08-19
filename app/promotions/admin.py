from django.contrib import admin

from .models import Booking, Promotion, Service

admin.site.register(Promotion)
admin.site.register(Booking)
admin.site.register(Service)