from django.urls import path

from .views import index, delivery

app_name = 'storedvd'
urlpatterns = [
    path('', index, name='index'),
    path('delivery', delivery, name='delivery'),
]
