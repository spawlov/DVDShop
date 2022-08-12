from django.urls import path

from . import views
from .views import Index

app_name = 'storedvd'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', Index.as_view(), name='index'),
]
