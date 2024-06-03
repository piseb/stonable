from django.urls import path
from . import views

APP_NAME = "stonable"

urlpatterns = [
    path("", views.home, name="home"),
    path("annuaire", views.annuaire, name="annuaire"),
    path("annuaire/entite/new", views.entite_create, name="entite_create"),
    path("annuaire/entite/<int:entite_id>", views.entite_read, name="entite_read"),
]
