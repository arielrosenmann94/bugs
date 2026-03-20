"""
URL configuration for pokedex project.
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin//', admin.site.urls),
    path('', include('pokemon.urls', namespace='pokemon')),
]
