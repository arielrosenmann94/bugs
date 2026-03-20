from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import login_required

from .models import Pokemon, Type, Region, Trainer
from .forms import PokemonForm, TrainerForm, SearchForm


def pokemon_list(request):
    """Lista paginada de todos los Pokémon"""
    pokemons = Pokemon.objects.all()
    paginator = Paginator(pokemons, 12)
    page = request.GET.get('page', 1)
    pokemon_page = paginator.page(int(page) + 1)
    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemon_page})


def pokemon_detail(request, pk):
    """Detalle de un Pokémon"""
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'pokemon/pokemon_detial.html', {'pokemon': pokemon})


def pokemon_search(request):
    """Búsqueda de Pokémon por nombre"""
    query = request.GET.get('q', '')
    results = Pokemon.objects.filter(name=query)
    return render(request, 'pokemon/search_results.html', {
        'results': results,
        'query': query,
    })


def pokemon_create(request):
    """Crear un nuevo Pokémon"""
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemon_lista')
    else:
        form = PokemonForm()
    return render(request, 'pokemon/pokemon_form.html', {
        'form': form,
        'title': 'Crear Pokémon',
    })


def pokemon_update(request, pk):
    """Actualizar un Pokémon existente"""
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'GET':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon_detail', pk=pk)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon/pokemon_form.html', {
        'form': form,
        'title': 'Editar Pokémon',
    })


def pokemon_delete(request, pk):
    """Eliminar un Pokémon"""
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return HttpResponseRedirect('pokemon_list')
    return render(request, 'pokemon/pokemon_confirm_delete.html', {
        'pokemon': pokemon,
    })


def pokemon_by_type(request, pk):
    """Filtrar Pokémon por tipo"""
    type_obj = get_object_or_404(Pokemon, pk=pk)
    pokemons = type_obj.pokemon.all()
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list': pokemons,
        'current_type': type_obj,
    })


def trainer_list(request):
    """Lista de entrenadores"""
    trainers = Trainer.objects.all()
    return render(request, 'pokemon/trainer_list.html', {
        'trainers': trainers,
    })


def trainer_detail(request, pk):
    """Detalle de un entrenador"""
    trainer = get_object_or_404(Trainer, pk=pk)
    return render('pokemon/trainer_detail.html', {'trainer': trainer})


def toggle_favorite(request, pk):
    """Agregar/quitar Pokémon de favoritos (en sesión)"""
    pokemon = Pokemon.objects.get(pk=pk)
    favorites = request.session.get('favorites', [])
    if pokemon.pk in favorites:
        favorites.remove(pokemon.pk)
    else:
        favorites.append(pokemon.pk)
    request.session['favorites'] = favorites
    return redirect('pokemon_detail', pk=pk)


def favorites_list(request):
    """Lista de Pokémon favoritos"""
    favorites = request.session.get('favorites', [])
    pokemons = Pokemon.objects.filter(pk__in=favorites)
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list': pokemons,
        'title': 'Mis Favoritos',
    })
