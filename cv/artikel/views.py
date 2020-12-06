from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArtikelForm, ArtikelModelForm
from .models import ArtikelModel
# Create your views here.

def CreateArtikelForm(request, *args, **kwargs):
    form = ArtikelModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        obj = form.save()
        # image = request.FILES['image']
        # obj.image = image
        obj.save()
        # my_form = form.cleaned_data
        # ArtikelModel.objects.create(**my_form)
        form = ArtikelModelForm()
        return redirect('list')
    return render(request, 'form.html', {'form': form})


def DetailArtikel(request, slug):
    qs = ArtikelModel.objects.filter(slug=slug)
    if qs.count() == 0:
        raise Http404
    obj = qs.first()
    # obj = get_object_or_404(ArtikelModel, slug=slug)

    return render(request, "artikel_detail.html", {"objek": obj})

def UpdateArtikel(request, slug):
    # qs = ArtikelModel.objects.filter(slug=slug)
    obj = get_object_or_404(ArtikelModel, slug=slug)
    form = ArtikelModelForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()

    return render(request, 'form.html', {'form': form})


def DeleteArtikel(request, slug):
    qs = ArtikelModel.objects.filter(slug=slug)
    if qs.count() == 0:
        raise Http404
    obj = qs.first()
    if request.method == 'POST':
        obj.delete()
        return redirect('list')

    return render(request, 'artikel_delete.html', {'objek': obj})


def ListArtikel(request, *args, **kwargs):
    obj = ArtikelModel.objects.all()

    return render(request, 'artikel_list.html', {'objek': obj})


def base(request, *args, **kwargs):
    return render(request, 'base.html',)