from django.shortcuts import render, get_object_or_404, redirect
from .models import Inscription
from .forms import InscriptionForm
# Create your views here.


def index(request):
    return render(request, "note/index.html", {
        "inscriptions": Inscription.objects.all()
    })


def inscription(request, id):
    inscription = get_object_or_404(Inscription, id=id)
    return render(request, "note/inscription.html", {
        "inscription": inscription
    })


def add(request):
    form = InscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("note:index")
    return render(request, "note/addinscription.html", {
        "form": form
    })


def update(request, id):
    inscription = Inscription.objects.get(id=id)
    form = InscriptionForm(request.POST or None, instance=inscription)
    if form.is_valid():
        form.save()
        return redirect("note:index")
    return render(request, "note/addinscription.html", {
        "form": form,
        "inscription": inscription
    })


def delete(request, id):
    inscription = Inscription.objects.get(id=id)
    if request.method == 'POST':
        inscription.delete()
        return redirect('note:index')
    return render(request, 'note/inscr-delete.html', {
        'inscription': inscription
    })




"""
def search(request):
    q = request.GET.get('q').strip()
    return render(request, "note/SearchResults.html", {
        "": util.search_results(q.lower()),
        "q": q
    })
"""