from django.urls import path
from . import views

APP_NAME = "stonable"

urlpatterns = [
    path("", views.home, name="home"),
    path("entites", views.entites, name="entites"),
    path("entites/new", views.entite_create_or_update, name="entite_create"),
    path("entites/<int:entite_id>", views.entite_create_or_update, name="entite_read"),
]
