from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('all/', views.pokemon_list, name='pokemon_list'),
    path('pokemon/<pk>/', views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/search/', views.pokemon_search, name='pokemon_search'),
    path('pokemon/create', views.pokemon_create, name='pokemon_create'),
    path('pokemon/<int:pk>/update/', views.pokemon_update, name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.pokemon_delete, name='pokemon_delete'),
    path('pokemon/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    re_path(r'type/(?P<pk>\d+)', views.pokemon_by_type, name='pokemon_by_type'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/<int:pk>/', views.trainer_detail, name='trainer_detail'),
]
