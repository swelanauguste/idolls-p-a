from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView

from .models import Banner, Social, Value, WhyUs


def home_view(request):
    context = {
        "values": Value.objects.all(),
        "whys": WhyUs.objects.all(),
        "socials": Social.objects.all(),
        "banners": Banner.objects.all(),
    }
    return render(request, "page/home.html", context)


class ValueListView(ListView):
    model = Value


class ValueDetailView(DetailView):
    model = Value


class ValueUpdateView(UpdateView):
    model = Value
    fields = ["image", "name", "desc", "sort"]
