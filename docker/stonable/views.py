from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .forms import EntiteForm
from .models import Entite


def home(request):
    return render(request, "home.html")


def entites(request):
    entites = Entite.objects.all()
    return render(request, "entites/entites.html", {"entites": entites})


def entite_create_or_update(request, entite_id=None):
    if entite_id:
        instance = get_object_or_404(Entite, pk=entite_id)
    else:
        instance = None

    if request.method == "POST":
        details = EntiteForm(request.POST, instance=instance)
        if details.is_valid():
            details.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(
                request,
                "entites/entite.html",
                {"form": details, "entite_id": entite_id},
            )
    else:
        form = EntiteForm(instance=instance)
        return render(
            request, "entites/entite.html", {"form": form, "entite_id": entite_id}
        )
