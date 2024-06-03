from django.http import HttpResponse

<<<<<<< HEAD

def index(request):
    return render(request, "index.html")
=======
def index():
    return HttpResponse("futur annuaire")
>>>>>>> 4f3d444 (adding basics urls and view)
