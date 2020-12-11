from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArtikelForm, ArtikelModelForm, CommentForm
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
    # qs = ArtikelModel.objects.filter(slug=slug)
    # if qs.count() == 0:
    #     raise Http404
    # obj = qs.first()
    obj = get_object_or_404(ArtikelModel, slug=slug)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_com = comment_form.save(commit=False)
        new_com.judul = obj
        new_com.save()
        return redirect("detail", slug = obj.slug)
    else:
        comment_form = CommentForm()
    return render(request, "artikel_detail.html", {"objek": obj, "comment_form": comment_form})

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
    paginator = Paginator(obj, 2)
    
    page_request = "page"
    page = request.GET.get(page_request)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    context = {
        "objek": obj,
        "page_request": page_request
    }

    return render(request, 'artikel_list.html', context)


def base(request, *args, **kwargs):
    return render(request, 'base.html',)
