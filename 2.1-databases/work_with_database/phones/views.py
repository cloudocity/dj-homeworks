from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort", 'name')
    if sort == 'name':
        context = {}
        context['phones'] = Phone.objects.order_by('name')
    elif sort == 'min_price':
        context = {}
        context['phones'] = Phone.objects.order_by('price')
    elif sort == 'max_price':
        context = {}
        context['phones'] = Phone.objects.order_by('-price')
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    context['phone'] = Phone.objects.get(slug=slug)
    return render(request, template, context)
