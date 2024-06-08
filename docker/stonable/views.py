from django.shortcuts import render


def home(request, alertes=None):
    context = {"alertes": alertes}
    return render(request, "home.html", context)
