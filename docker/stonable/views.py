from django.shortcuts import render


def home(request, alertes=None):
    return render(request, "home.html", context)
