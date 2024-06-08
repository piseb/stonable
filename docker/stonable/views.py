from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import EntiteForm
from .models import Entite


def home(request):
    return render(request, "home.html")


def entites(request):
    context = {}
    # TODO optimiser le query
    entites = Entite.objects.all()
    paginator = Paginator(entites, 10)

    page_current = request.GET.get("page")
    if page_current:
        page_current = int(page_current)
    else:
        page_current = 1
    context["page_current"] = page_current

    entites = paginator.get_page(page_current)
    context["entites"] = entites

    context["pages"] = paginator.page_range

    if entites.has_next():
        page_next = page_current + 1
    else:
        page_next = None
    context["page_next"] = page_next

    if entites.has_previous():
        page_previous = page_current - 1
    else:
        page_previous = None
    context["page_previous"] = page_previous

    return render(request, "entites/entites.html", context)


def entite_create_or_update(request, entite_id=None):
    context = {"entite_id": entite_id}
    if entite_id:
        instance = get_object_or_404(Entite, pk=entite_id)
    else:
        instance = None

    if request.method == "POST":
        details = EntiteForm(request.POST, instance=instance)
        context["form"] = details
        if details.is_valid():
            details.save()
            messages.success(request, "Nouvelle entité Enregistrée." )
            return redirect(entites)
        else:
            return render(request, context)
    else:
        form = EntiteForm(instance=instance)
        context["form"] = form
        return render(request, "entites/entite.html", context)



def entite_delete(request, entite_id):
    entite = get_object_or_404(Entite, pk=entite_id)
    entite.delete()
    return redirect(entites)
