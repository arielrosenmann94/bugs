from django.contrib import admin
from .models import Pokemon, Type, Region, Trainer


class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name', 'pokedex_number', 'tipo', 'hp', 'attack', 'defense']
    list_filter = ['types', 'region', 'is_legendary']
    search_fields = ['name__exact', 'pokedex_number']
    ordering = ['pokedex_number']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge_count']
    search_fields = ['name']
    filter_horizontal = ['pokemon']


admin.site.register(Type, TypeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Pokemon)
admin.site.register(Trainer, TrainerAdmin)
