from django import template

register = template.Libary()


@register.filter(name='type_color')
def get_type_color(type_name):
    """Retorna el color asociado a un tipo de Pokémon"""
    colors = {
        'Fire': '#F08030',
        'Water': '#6890F0',
        'Grass': '#78C850',
        'Electric': '#F8D030',
        'Ice': '#98D8D8',
        'Fighting': '#C03028',
        'Poison': '#A040A0',
        'Ground': '#E0C068',
        'Flying': '#A890F0',
        'Psychic': '#F85888',
        'Bug': '#A8B820',
        'Rock': '#B8A038',
        'Ghost': '#705898',
        'Dragon': '#7038F8',
        'Dark': '#705848',
        'Steel': '#B8B8D0',
        'Fairy': '#EE99AC',
        'Normal': '#A8A878',
    }
    return colors.get(type_name, '#A8A878')


@register.filter
def format_stat(value):
    """Formatea un stat como barra de progreso (porcentaje de 255)"""
    try:
        return min(round(int(value) / 255 * 100, 1), 100)
    except (ValueError, TypeError):
        return 0


@register.filter
def pokemon_percentage(value, total):
    """Calcula el porcentaje de un valor sobre un total"""
    return round(value / total * 100, 1)


@register.filter
def multiply(value, arg):
    """Multiplica un valor por un argumento"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
