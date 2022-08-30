from django.shortcuts import render
from django.template import context
from django.views.generic import ListView

from .models import Product, Section


class Index(ListView):
    # model = Product
    queryset = Product.objects.all()[:8]
    template_name = 'index.html'
    context_object_name = 'products'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        contexts = super(Index, self).get_context_data(**kwargs)
        contexts['sections'] = Section.objects.order_by('title').all()
        return contexts


# def index(request):
#     sections = Section.objects.all()
#     context = {'sections': sections}
#     return render(request, 'index.html', context=context)
