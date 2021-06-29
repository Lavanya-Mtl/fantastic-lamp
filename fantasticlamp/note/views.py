from django.shortcuts import render, get_object_or_404
from .models import Inscription
# Create your views here.


def index(request):
    return render(request, "note/index.html", {
        "inscriptions": Inscription.objects.all()
    })


def inscription(request, title):
    inscription = get_object_or_404(Inscription, title=title)
    return render(request, "note/inscription.html", {
        "inscription": inscription
    })



"""
def search(request):
    q = request.GET.get('q').strip()
    return render(request, "note/SearchResults.html", {
        "": util.search_results(q.lower()),
        "q": q
    })
"""