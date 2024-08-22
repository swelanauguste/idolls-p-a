from django.contrib import admin

# Register your models here.
from .models import Banner, Social, Value, WhyUs

admin.site.register(Value)
admin.site.register(WhyUs)
admin.site.register(Social)
admin.site.register(Banner)
