from django.shortcuts import render
from django.contrib import messages


def home(request):
    messages.success(request, "Message sent.")
    return render(request, "home.html")
