from django.shortcuts import render
from django.template import context
from django.views.generic import ListView

from .models import Product


class Index(ListView):
    model = Product
    template_name = 'index.html'
    ...
# def index(request):
#     return render(request, 'index.html')
