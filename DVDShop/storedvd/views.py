from django.shortcuts import render
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
    sections = Section.objects.order_by('title').all()
    products = Product.objects.order_by(sorted_title_or_price(request)).all()[:8]
    context = {
        'sections': sections,
        'products': products,
    }
    return render(request, 'index.html', context=context)
