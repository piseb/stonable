from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .forms import EntiteForm
from .models import Entite


def home(request):
    return render(request, "home.html")


def entites(request):
    entites = Entite.objects.all()
    return render(request, "annuaire/index.html", {"entites": entites})


def entite_read(request, entite_id):
    entite = get_object_or_404(Entite, pk=entite_id)
    form = EntiteForm(instance=entite)
    return render(request, "annuaire/entite.html", {"form": form})


def entite_create(request):
    if request.method == "POST":
        details = EntiteForm(request.POST)
        if details.is_valid():
            details.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, "annuaire/entite.html", {"form": details})
    else:
        form = EntiteForm()
        return render(request, "annuaire/entite.html", {"form": form})
