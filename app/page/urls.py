from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="value-list"),
    path("detail/<int:pk>/", views.ValueDetailView.as_view(), name="value-detail"),
    path("update/<int:pk>/", views.ValueUpdateView.as_view(), name="value-update"),
]
