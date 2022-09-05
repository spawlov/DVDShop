from django.shortcuts import render, get_object_or_404
from django.template import context
from django.views.generic import ListView

from .models import Product, Section


def sorted_title_or_price(request):
    order_by = '-date'
    if all([request.GET.__contains__('sort'), request.GET.__contains__('up')]):
        if all([
            any([request.GET['sort'] == 'title', request.GET['sort'] == 'price']),
            any([request.GET['up'] == '0', request.GET['up'] == '1']),
        ]):
            order_by = f'{"" if request.GET["up"] == "1" else "-"}{request.GET["sort"]}'
    return order_by


def index(request):
    products = Product.objects.order_by(sorted_title_or_price(request)).all()[:8]
    context = {
        'products': products,
    }
    return render(request, 'index.html', context=context)


def delivery(request):
    return render(request, 'delivery.html')


def contacts(request):
    return render(request, 'contacts.html')


def section(request, id):
    obj = get_object_or_404(Section, pk=id)
    products = Product.objects.filter(section__exact=obj).order_by(
        sorted_title_or_price(request)
    )
    context = {
        'section': obj,
        'products': products,
    }
    return render(request, 'section.html', context=context)
