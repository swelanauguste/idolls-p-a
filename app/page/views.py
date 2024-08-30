from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView

from .models import Banner, Service, Social, Value, WhyUs


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
