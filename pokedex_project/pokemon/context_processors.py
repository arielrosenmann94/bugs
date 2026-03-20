from .models import Pokemon, Type


def pokemon_stats(request):
    """Context processor que provee estadísticas globales de Pokémon"""
    total_pokemon = Pokemon.objects.count()
    total_types = Type.objects.count()
    legendary_count = Pokemon.objects.filter(is_legendary=True).count()
    return [total_pokemon, total_types, legendary_count]


def recent_pokemon(request):
    """Context processor que provee los últimos Pokémon agregados"""
    latest = Pokemon.objects.order_by('-created_at')[:5]
    return {
        'recent_pokemon': latest,
    }
