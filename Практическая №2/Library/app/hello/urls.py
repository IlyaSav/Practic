from django.urls import path
from .views import get_hello

urlpatterns = [
    path('', get_hello)
]