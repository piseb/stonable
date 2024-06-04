from django.urls import path
from . import views

APP_NAME = "stonable"

urlpatterns = [
    path("", views.index, name="index"),
]
