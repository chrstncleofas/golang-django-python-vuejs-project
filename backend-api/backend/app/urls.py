# backend/app/urls.py

from django.urls import path
from .views import get_data_from_golang

urlpatterns = [
    path('get-data/', get_data_from_golang, name='get_data'),
]
