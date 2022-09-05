from django.urls import path

from .views import index, delivery, contacts, section

app_name = 'storedvd'
urlpatterns = [
    path('', index, name='index'),
    path('delivery', delivery, name='delivery'),
    path('contacts', contacts, name='contacts'),
    path('section/<int:id>/', section, name='section'),
]
