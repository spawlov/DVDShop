from django.urls import path

from .views import index, delivery, contacts

app_name = 'storedvd'
urlpatterns = [
    path('', index, name='index'),
    path('delivery', delivery, name='delivery'),
    path('contacts', contacts, name='contacts'),
]
