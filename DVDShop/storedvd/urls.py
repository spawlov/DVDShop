from django.urls import path

from .views import index
# from .views import Index

app_name = 'storedvd'
urlpatterns = [
    path('', index, name='index'),
]
