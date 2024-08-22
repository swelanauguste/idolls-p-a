from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, UpdateView

from .models import Social, Value, WhyUs, Banner


class Home(TemplateView):
    template_name = "page/home.html"

    extra_context = {
        "values": Value.objects.all(),
        "whys": WhyUs.objects.all(),
        "socials": Social.objects.all(),
        "banners": Banner.objects.all(),
    }


class ValueListView(ListView):
    model = Value


class ValueDetailView(DetailView):
    model = Value


class ValueUpdateView(UpdateView):
    model = Value
    fields = ["image", "name", "desc", "sort"]
