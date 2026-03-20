from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type, Region, Trainer


class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de Pokémon de ejemplo'

    def handle(self, *args, **options):
        self.stdout.write('🔄 Creando tipos de Pokémon...')
        types_data = [
            {'name': 'Fire', 'color': '#F08030'},
            {'name': 'Water', 'color': '#6890F0'},
            {'name': 'Grass', 'color': '#78C850'},
            {'name': 'Electric', 'color': '#F8D030'},
            {'name': 'Ice', 'color': '#98D8D8'},
            {'name': 'Fighting', 'color': '#C03028'},
            {'name': 'Poison', 'color': '#A040A0'},
            {'name': 'Ground', 'color': '#E0C068'},
            {'name': 'Flying', 'color': '#A890F0'},
            {'name': 'Psychic', 'color': '#F85888'},
            {'name': 'Bug', 'color': '#A8B820'},
            {'name': 'Rock', 'color': '#B8A038'},
            {'name': 'Ghost', 'color': '#705898'},
            {'name': 'Dragon', 'color': '#7038F8'},
            {'name': 'Dark', 'color': '#705848'},
            {'name': 'Steel', 'color': '#B8B8D0'},
            {'name': 'Fairy', 'color': '#EE99AC'},
            {'name': 'Normal', 'color': '#A8A878'},
        ]
        types = {}
        for t in types_data:
            obj, _ = Type.objects.get_or_create(**t)
            types[t['name']] = obj

        self.stdout.write('🔄 Creando regiones...')
        regions_data = [
            {'name': 'Kanto', 'description': 'La región original donde todo comenzó.'},
            {'name': 'Johto', 'description': 'Región conectada a Kanto al oeste.'},
            {'name': 'Hoenn', 'description': 'Región tropical con mucha agua.'},
        ]
        regions = {}
        for r in regions_data:
            obj, _ = Region.objects.get_or_create(**r)
            regions[r['name']] = obj

        self.stdout.write('🔄 Creando Pokémon...')
        sprite_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png'
        pokemon_data = [
            {'name': 'Bulbasaur', 'pokedex_number': 1, 'region': 'Kanto', 'types': ['Grass', 'Poison'],
             'hp': 45, 'attack': 49, 'defense': 49, 'speed': 45, 'height': 0.7, 'weight': 6.9,
             'description': 'Una semilla extraña fue plantada en su espalda al nacer.'},
            {'name': 'Charmander', 'pokedex_number': 4, 'region': 'Kanto', 'types': ['Fire'],
             'hp': 39, 'attack': 52, 'defense': 43, 'speed': 65, 'height': 0.6, 'weight': 8.5,
             'description': 'Prefiere las cosas calientes. Dicen que cuando llueve, le sale vapor de la punta de la cola.'},
            {'name': 'Squirtle', 'pokedex_number': 7, 'region': 'Kanto', 'types': ['Water'],
             'hp': 44, 'attack': 48, 'defense': 65, 'speed': 43, 'height': 0.5, 'weight': 9.0,
             'description': 'Cuando retrae su largo cuello en el caparazón, lanza agua a gran presión.'},
            {'name': 'Pikachu', 'pokedex_number': 25, 'region': 'Kanto', 'types': ['Electric'],
             'hp': 35, 'attack': 55, 'defense': 40, 'speed': 90, 'height': 0.4, 'weight': 6.0,
             'description': 'Cuando varios de estos Pokémon se juntan, su energía puede causar tormentas.'},
            {'name': 'Jigglypuff', 'pokedex_number': 39, 'region': 'Kanto', 'types': ['Normal', 'Fairy'],
             'hp': 115, 'attack': 45, 'defense': 20, 'speed': 20, 'height': 0.5, 'weight': 5.5,
             'description': 'Cuando sus grandes ojos se iluminan, canta una melodía que hace dormir.'},
            {'name': 'Gengar', 'pokedex_number': 94, 'region': 'Kanto', 'types': ['Ghost', 'Poison'],
             'hp': 60, 'attack': 65, 'defense': 60, 'speed': 110, 'height': 1.5, 'weight': 40.5,
             'description': 'Se esconde en las sombras. Dicen que si sientes frío, es porque Gengar está cerca.'},
            {'name': 'Gyarados', 'pokedex_number': 130, 'region': 'Kanto', 'types': ['Water', 'Flying'],
             'hp': 95, 'attack': 125, 'defense': 79, 'speed': 81, 'height': 6.5, 'weight': 235.0,
             'description': 'Brutalmente vicioso y enormemente destructivo. Conocido por reducir ciudades a cenizas.'},
            {'name': 'Eevee', 'pokedex_number': 133, 'region': 'Kanto', 'types': ['Normal'],
             'hp': 55, 'attack': 55, 'defense': 50, 'speed': 55, 'height': 0.3, 'weight': 6.5,
             'description': 'Su código genético irregular le permite evolucionar en múltiples formas.'},
            {'name': 'Snorlax', 'pokedex_number': 143, 'region': 'Kanto', 'types': ['Normal'],
             'hp': 160, 'attack': 110, 'defense': 65, 'speed': 30, 'height': 2.1, 'weight': 460.0,
             'description': 'Muy perezoso. Come y duerme todo el día. Necesita 400 kg de comida diaria.'},
            {'name': 'Mewtwo', 'pokedex_number': 150, 'region': 'Kanto', 'types': ['Psychic'],
             'hp': 106, 'attack': 110, 'defense': 90, 'speed': 130, 'height': 2.0, 'weight': 122.0,
             'description': 'Fue creado por un científico tras años de manipulación genética.', 'is_legendary': True},
            {'name': 'Chikorita', 'pokedex_number': 152, 'region': 'Johto', 'types': ['Grass'],
             'hp': 45, 'attack': 49, 'defense': 65, 'speed': 45, 'height': 0.9, 'weight': 6.4,
             'description': 'Un dulce aroma se desprende de la hoja en su cabeza.'},
            {'name': 'Cyndaquil', 'pokedex_number': 155, 'region': 'Johto', 'types': ['Fire'],
             'hp': 39, 'attack': 52, 'defense': 43, 'speed': 65, 'height': 0.5, 'weight': 7.9,
             'description': 'Es tímido y siempre se acurruca. Cuando se asusta, las llamas de su espalda arden más.'},
            {'name': 'Totodile', 'pokedex_number': 158, 'region': 'Johto', 'types': ['Water'],
             'hp': 50, 'attack': 65, 'defense': 64, 'speed': 43, 'height': 0.6, 'weight': 9.5,
             'description': 'Sus mandíbulas son fuertes. Tiene la costumbre de morder todo lo que ve.'},
            {'name': 'Lugia', 'pokedex_number': 249, 'region': 'Johto', 'types': ['Psychic', 'Flying'],
             'hp': 106, 'attack': 90, 'defense': 130, 'speed': 110, 'height': 5.2, 'weight': 216.0,
             'description': 'Se dice que es el guardián de los mares. Se le ha visto en tormentas.', 'is_legendary': True},
            {'name': 'Treecko', 'pokedex_number': 252, 'region': 'Hoenn', 'types': ['Grass'],
             'hp': 40, 'attack': 45, 'defense': 35, 'speed': 70, 'height': 0.5, 'weight': 5.0,
             'description': 'Los ganchos de sus patas le permiten caminar por paredes y techos.'},
            {'name': 'Torchic', 'pokedex_number': 255, 'region': 'Hoenn', 'types': ['Fire'],
             'hp': 45, 'attack': 60, 'defense': 40, 'speed': 45, 'height': 0.4, 'weight': 2.5,
             'description': 'Tiene una llama dentro de su cuerpo. Si lo abrazas sentirás su calidez.'},
            {'name': 'Mudkip', 'pokedex_number': 258, 'region': 'Hoenn', 'types': ['Water'],
             'hp': 50, 'attack': 70, 'defense': 50, 'speed': 40, 'height': 0.4, 'weight': 7.6,
             'description': 'La aleta en su cabeza funciona como radar para detectar movimientos en el agua.'},
            {'name': 'Rayquaza', 'pokedex_number': 384, 'region': 'Hoenn', 'types': ['Dragon', 'Flying'],
             'hp': 105, 'attack': 150, 'defense': 90, 'speed': 95, 'height': 7.0, 'weight': 206.5,
             'description': 'Vive en la capa de ozono y nunca baja al suelo.', 'is_legendary': True},
            {'name': 'Gardevoir', 'pokedex_number': 282, 'region': 'Hoenn', 'types': ['Psychic', 'Fairy'],
             'hp': 68, 'attack': 65, 'defense': 65, 'speed': 80, 'height': 1.6, 'weight': 48.4,
             'description': 'Tiene el poder de predecir el futuro. Protegerá a su entrenador con su vida.'},
            {'name': 'Lucario', 'pokedex_number': 448, 'region': 'Kanto', 'types': ['Fighting', 'Steel'],
             'hp': 70, 'attack': 110, 'defense': 70, 'speed': 90, 'height': 1.2, 'weight': 54.0,
             'description': 'Puede percibir el aura de todas las cosas. Entiende el lenguaje humano.'},
        ]

        for p_data in pokemon_data:
            type_names = p_data.pop('types')
            region_name = p_data.pop('region')
            p_data['region'] = regions[region_name]
            p_data['image_url'] = sprite_url.format(p_data['pokedex_number'])
            pokemon, created = Pokemon.objects.get_or_create(
                pokedex_number=p_data['pokedex_number'],
                defaults=p_data
            )
            if created:
                for t_name in type_names:
                    pokemon.types.add(types[t_name])

        self.stdout.write('🔄 Creando entrenadores...')
        trainers_data = [
            {'name': 'Ash Ketchum', 'badge_count': 8,
             'pokemon_names': ['Pikachu', 'Charizard', 'Bulbasaur', 'Squirtle', 'Snorlax', 'Lucario']},
            {'name': 'Misty', 'badge_count': 4,
             'pokemon_names': ['Gyarados', 'Squirtle']},
            {'name': 'Brock', 'badge_count': 2,
             'pokemon_names': ['Snorlax']},
        ]
        for t_data in trainers_data:
            pokemon_names = t_data.pop('pokemon_names')
            trainer, created = Trainer.objects.get_or_create(
                name=t_data['name'],
                defaults=t_data
            )
            if created:
                for p_name in pokemon_names:
                    try:
                        pokemon = Pokemon.objects.get(name=p_name)
                        trainer.pokemon.add(pokemon)
                    except Pokemon.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'  ⚠️ Pokémon "{p_name}" no encontrado'))

        total = Pokemon.objects.count()
        self.stdout.write(self.style.SUCCESS(f'✅ Seed completado: {total} Pokémon creados'))
