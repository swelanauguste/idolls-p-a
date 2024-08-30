from django.urls import path

from . import views

urlpatterns = [
    # path("", views.Home.as_view(), name="value-list"),
    path("", views.home_view, name="value-list"),
    path("services-list", views.services_view, name="services-list"),
    path("footer", views.services_view, name="footer"),
]
