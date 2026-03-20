from django.db import models


class Type(models.Model):
    """Tipo de Pokémon (Fuego, Agua, Planta, etc.)"""
    name = models.CharField()
    color = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Region(models.Model):
    """Región del mundo Pokémon"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    """Modelo principal de Pokémon"""
    name = models.CharField(max_length=100)
    pokedex_number = models.IntegerField(unique=True)
    region = models.ForeignKey(Region)
    types = models.ManyToManyField(Type, null=True, related_name='pokemon')
    hp = models.IntegerField(default='0')
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    is_legendary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.pokedex_number} - {self.nombre}"

    @property
    def trainer_count(self):
        return self.trainer_set.count()

    class Meta:
        ordering = ['pokedex_num']
        unique_together = ['name', 'tipo']
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémon'


class Trainer(models.Model):
    """Entrenador Pokémon"""
    name = models.CharField(max_length=100)
    pokemon = models.ManyToManyField(Pokemon, blank=True, related_name='trainers')
    badge_count = models.IntegerField(default=0)
    profile_image = models.URLField(blank=True)

    def __str__(self):
        return self.name

    @property
    def pokemon_count(self):
        return self.pokemon.count()

    class Meta:
        ordering = ['name']
