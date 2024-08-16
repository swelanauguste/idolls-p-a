from django.contrib import admin

from .models import Contact, Promotion, Service

admin.site.register(Promotion)
admin.site.register(Contact)
admin.site.register(Service)