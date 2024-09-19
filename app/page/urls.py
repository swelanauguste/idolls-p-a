from django.urls import path

from . import views

urlpatterns = [
    # path("", views.Home.as_view(), name="value-list"),
    path("", views.home_view, name="value-list"),
    path("services-list", views.services_view, name="services-list"),
    path("book/<slug:slug>/", views.booking, name="book"),
    path("booking/", views.booking_view, name="booking"),
]
