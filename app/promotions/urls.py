from django.urls import path

from . import views

urlpatterns = [
    path("", views.PromotionListView.as_view(), name="list"),
    path("create/", views.PromotionCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", views.PromotionDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.PromotionUpdateView.as_view(), name="update"),
    path("booking", views.booking_view, name="booking"),
]
