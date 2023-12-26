from django.urls import path

from . import views

urlpatterns = [
    path("losses", views.get_losses, name="get_losses"),
]