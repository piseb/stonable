from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import EntiteForm
from .models import Entite


def home(request):
    return render(request, "home.html")


def entites(request):
    # TODO optimiser le query
    entites = Entite.objects.all()
    paginator = Paginator(entites, 10)

    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 1

    entites = paginator.get_page(page)
    pages = paginator.page_range

    if entites.has_next():
        page_next = page + 1
    else:
        page_next = None

    if entites.has_previous():
        page_previous = page - 1
    else:
        page_previous = None

    return render(
        request,
        "entites/entites.html",
        {
            "entites": entites,
            "page_current": page,
            "page_next": page_next,
            "page_previous": page_previous,
            "pages": pages,
        },
    )


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


def entite_delete(request, entite_id):
    entite = get_object_or_404(Entite, pk=entite_id)
    entite.delete()
    return redirect(entites)
