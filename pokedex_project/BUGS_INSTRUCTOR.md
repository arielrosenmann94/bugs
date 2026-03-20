# 🐛 Guía del Instructor - 50 Bugs de la Pokédex

## Resumen

| Categoría | Cantidad | Dificultad |
|---|---|---|
| Settings | 4 | 🟢🟢 🟡 🔴 |
| URLs proyecto | 3 | 🟢🟢 🟡 |
| Modelos | 8 | 🟢🟢🟢 🟡🟡🟡 🔴🔴 |
| Vistas | 10 | 🟢🟢🟢 🟡🟡🟡🟡 🔴🔴🔴 |
| URLs app | 4 | 🟢🟢 🟡 🔴 |
| Formularios | 5 | 🟢🟢 🟡 🔴🔴 |
| Admin | 3 | 🟢 🟡🟡 |
| Context processors | 2 | 🟡 🔴 |
| Template tags | 3 | 🟢 🟡 🔴 |
| Templates | 8 | 🟢🟢🟢 🟡🟡🟡 🔴🔴 |
| **Total** | **50** | **🟢19  🟡18  🔴13** |

---

## 🟢 = Fácil (1-2 min) | 🟡 = Medio (3-5 min) | 🔴 = Difícil (5-10 min)

---

## Settings (`config/settings.py`)

### Bug 1 🟢 — App mal registrada
- **Línea ~28:** `'pokemons'` debería ser `'pokemon'`
- **Error:** `ModuleNotFoundError: No module named 'pokemons'`
- **Fix:** Cambiar a `'pokemon'`

### Bug 2 🟡 — Directorio de templates incorrecto
- **Línea ~46:** `os.path.join(BASE_DIR, 'template')` (falta la 's')
- **Error:** Django no encuentra templates en DIRS (usa APP_DIRS como fallback, puede causar confusión)
- **Fix:** Cambiar `'template'` a `'templates'`

### Bug 3 🟢 — STATIC_URL sin trailing slash
- **Línea ~82:** `STATIC_URL = 'static'`
- **Error:** Los archivos estáticos no cargan correctamente
- **Fix:** Cambiar a `STATIC_URL = '/static/'` o `'static/'`

### Bug 4 🔴 — Orden de middleware incorrecto
- **Línea ~33-37:** `AuthenticationMiddleware` está ANTES de `SessionMiddleware`
- **Error:** `AssertionError: The Django authentication middleware requires session middleware to be installed`
- **Fix:** Mover `SessionMiddleware` antes de `AuthenticationMiddleware`

---

## URLs Proyecto (`config/urls.py`)

### Bug 5 🟢 — Falta import de include
- **Línea 5:** `from django.urls import path` (falta `include`)
- **Error:** `NameError: name 'include' is not defined`
- **Fix:** `from django.urls import path, include`

### Bug 6 🟢 — Doble slash en ruta admin
- **Línea 8:** `path('admin//', admin.site.urls)`
- **Error:** Admin accesible en `/admin//` en vez de `/admin/`
- **Fix:** `path('admin/', admin.site.urls)`

### Bug 7 🟡 — Namespace sin app_name en la app
- **Línea 9:** `include('pokemon.urls', namespace='pokemon')` pero `pokemon/urls.py` no tiene `app_name`
- **Error:** `ImproperlyConfigured: Specifying a namespace requires providing an app_name`
- **Fix:** Agregar `app_name = 'pokemon'` en `pokemon/urls.py` O quitar el `namespace='pokemon'`

---

## Modelos (`pokemon/models.py`)

### Bug 8 🟢 — CharField sin max_length
- **Línea 7:** `name = models.CharField()` en el modelo Type
- **Error:** `SystemCheckError: CharFields must define a 'max_length' attribute`
- **Fix:** `name = models.CharField(max_length=50)`

### Bug 9 🟢 — ForeignKey sin on_delete
- **Línea 34:** `region = models.ForeignKey(Region)`
- **Error:** `TypeError: __init__() missing required keyword argument: 'on_delete'`
- **Fix:** `region = models.ForeignKey(Region, on_delete=models.CASCADE)`

### Bug 10 🟡 — ManyToManyField con null=True
- **Línea 35:** `types = models.ManyToManyField(Type, null=True, ...)`
- **Error:** `null` no tiene efecto en ManyToManyField (warning en check)
- **Fix:** Quitar `null=True`

### Bug 11 🟡 — __str__ usa atributo inexistente
- **Línea 46:** `self.nombre` pero el campo es `self.name`
- **Error:** `AttributeError: 'Pokemon' object has no attribute 'nombre'`
- **Fix:** Cambiar `self.nombre` a `self.name`

### Bug 12 🟢 — Default de IntegerField como string
- **Línea 36:** `hp = models.IntegerField(default='0')`
- **Error:** puede causar problemas de tipo en comparaciones
- **Fix:** `default=0` (entero, no string)

### Bug 13 🟡 — Meta.ordering con campo inexistente
- **Línea 51:** `ordering = ['pokedex_num']`
- **Error:** `FieldDoesNotExist: Pokemon has no field named 'pokedex_num'`
- **Fix:** `ordering = ['pokedex_number']`

### Bug 14 🔴 — unique_together con campo inexistente
- **Línea 52:** `unique_together = ['name', 'tipo']`
- **Error:** `FieldDoesNotExist` en migración
- **Fix:** `unique_together = ['name', 'region']` o quitar la restricción

### Bug 15 🔴 — Property usa related manager incorrecto
- **Línea 49:** `self.trainer_set.count()` pero related_name es `'trainers'`
- **Error:** `AttributeError` al acceder a trainer_count
- **Fix:** `self.trainers.count()`

---

## Vistas (`pokemon/views.py`)

### Bug 16 🟢 — Import incorrecto de login_required
- **Línea 4:** `from django.contrib.auth.forms import login_required`
- **Error:** `ImportError: cannot import name 'login_required'`
- **Fix:** `from django.contrib.auth.decorators import login_required`

### Bug 17 🔴 — Paginación off-by-one
- **Línea 16:** `paginator.page(int(page) + 1)` la página 1 se convierte en página 2
- **Error:** `EmptyPage` o muestra la página equivocada
- **Fix:** `paginator.page(int(page))`

### Bug 18 🟡 — Variable de contexto no coincide con template
- **Línea 17:** `{'pokemons': pokemon_page}` pero template usa `pokemon_list`
- **Error:** Template muestra "No se encontraron Pokémon" aunque existan
- **Fix:** Cambiar `'pokemons'` a `'pokemon_list'`

### Bug 19 🟢 — Typo en nombre del template
- **Línea 23:** `'pokemon/pokemon_detial.html'` (detial → detail)
- **Error:** `TemplateDoesNotExist`
- **Fix:** `'pokemon/pokemon_detail.html'`

### Bug 20 🟡 — Búsqueda con filtro exacto
- **Línea 29:** `Pokemon.objects.filter(name=query)` busca coincidencia exacta
- **Error:** La búsqueda casi nunca encuentra resultados
- **Fix:** `Pokemon.objects.filter(name__icontains=query)`

### Bug 21 🟡 — Redirect a URL inexistente
- **Línea 38:** `redirect('pokemon_lista')` el name correcto es `'pokemon_list'`
- **Error:** `NoReverseMatch`
- **Fix:** `redirect('pokemon_list')`

### Bug 22 🔴 — Update compara con 'GET' en vez de 'POST'
- **Línea 48:** `if request.method == 'GET'` para guardar datos
- **Error:** El formulario nunca guarda; intenta guardar al cargar la página (sin datos POST)
- **Fix:** `if request.method == 'POST'`

### Bug 23 🟡 — Delete usa string literal en vez de reverse()
- **Línea 60:** `return HttpResponseRedirect('pokemon_list')` redirige a ruta literal `/pokemon_list`
- **Error:** 404 después de eliminar
- **Fix:** `from django.urls import reverse; return HttpResponseRedirect(reverse('pokemon_list'))`

### Bug 24 🟡 — get_object_or_404 con modelo incorrecto
- **Línea 65:** `get_object_or_404(Pokemon, pk=pk)` debería ser `Type`
- **Error:** Busca un Pokémon en vez de un Type para filtrar
- **Fix:** `get_object_or_404(Type, pk=pk)`

### Bug 25 🟢 — Falta request en render()
- **Línea 78:** `return render('pokemon/trainer_detail.html', {...})` sin request
- **Error:** `TypeError` o resultado incorrecto
- **Fix:** `return render(request, 'pokemon/trainer_detail.html', {...})`

### Bug 26 🟡 — No maneja DoesNotExist
- **Línea 83:** `Pokemon.objects.get(pk=pk)` sin try/except
- **Error:** Error 500 si el pk no existe
- **Fix:** Usar `get_object_or_404(Pokemon, pk=pk)`

---

## URLs App (`pokemon/urls.py`)

### Bug 27 🟢 — pk sin type converter
- **Línea 7:** `<pk>` debería ser `<int:pk>`
- **Error:** pk se recibe como string, puede causar errores en queries
- **Fix:** `<int:pk>`

### Bug 28 🟡 — Nombre de URL duplicado
- **Línea 5 y 6:** Dos rutas con `name='pokemon_list'`
- **Error:** Una URL siempre resuelve a la última registrada
- **Fix:** Renombrar una, ej: `name='pokemon_list_all'`

### Bug 29 🟢 — Falta trailing slash
- **Línea 8:** `path('pokemon/create', ...)` sin `/` al final
- **Error:** Con APPEND_SLASH=True causa redirect 301 innecesario
- **Fix:** `path('pokemon/create/', ...)`

### Bug 30 🔴 — re_path con regex incompleto
- **Línea 13:** `re_path(r'type/(?P<pk>\d+)', ...)` sin `^` ni trailing slash
- **Error:** Puede matchear rutas inesperadas
- **Fix:** `path('type/<int:pk>/', ...)` o `re_path(r'^type/(?P<pk>\d+)/$', ...)`

---

## Formularios (`pokemon/forms.py`)

### Bug 31 🟢 — TrainerForm hereda de forms.Form
- **Línea 6:** `class TrainerForm(forms.Form)` debería ser `forms.ModelForm`
- **Error:** La clase Meta es ignorada; el form no tiene campos
- **Fix:** `class TrainerForm(forms.ModelForm)`

### Bug 32 🟢 — fields con typo
- **Línea 21:** `fields = '__all_'` falta un underscore
- **Error:** `FieldError` o `TypeError`
- **Fix:** `fields = '__all__'`

### Bug 33 🟡 — Widget para campo inexistente
- **Línea 23:** `'nombre'` debería ser `'name'`
- **Error:** Widget no se aplica, campo renderiza sin estilos
- **Fix:** Cambiar `'nombre'` a `'name'`

### Bug 34 🔴 — ValueError en vez de ValidationError
- **Línea 40-43:** `raise ValueError(...)` en `clean_hp`
- **Error:** Error 500 con ValueError en vez de mostrar error en form
- **Fix:** `raise forms.ValidationError(...)`

### Bug 35 🔴 — clean_description para campo que puede no estar en fields
- **Línea 34-37:** `clean_description` existe pero si fields no incluye 'description', nunca se ejecuta
- **Error:** Validación silenciosamente ignorada
- **Fix:** Asegurar que 'description' esté en fields, o quitar el clean method

---

## Admin (`pokemon/admin.py`)

### Bug 36 🟢 — Campo inexistente en list_display
- **Línea 7:** `'tipo'` no es campo del modelo
- **Error:** Error al cargar admin de Pokemon
- **Fix:** Quitar `'tipo'` o reemplazar por campo válido

### Bug 37 🟡 — Modelo registrado dos veces
- **Línea 32-33:** `Pokemon` se registra con `PokemonAdmin` y luego sin él
- **Error:** `AlreadyRegistered: The model Pokemon is already registered`
- **Fix:** Quitar la segunda línea `admin.site.register(Pokemon)`

### Bug 38 🟡 — search_fields con lookup
- **Línea 9:** `'name__exact'` en search_fields
- **Error:** Búsqueda en admin no funciona correctamente
- **Fix:** `'name'` (sin lookup)

---

## Context Processors (`pokemon/context_processors.py`)

### Bug 39 🟡 — Retorna lista en vez de diccionario
- **Línea 9:** `return [total_pokemon, total_types, legendary_count]`
- **Error:** `TypeError: context must be a dict rather than list`
- **Fix:** `return {'pokemon_count': total_pokemon, 'type_count': total_types, 'legendary_count': legendary_count}`

### Bug 40 🔴 — Context processors no registrados en settings
- **Archivo:** `config/settings.py` → TEMPLATES → context_processors
- **Error:** Variables como `{{ pokemon_count }}` no están disponibles en templates
- **Fix:** Agregar `'pokemon.context_processors.pokemon_stats'` y `'pokemon.context_processors.recent_pokemon'` a la lista de context_processors en settings

---

## Template Tags (`pokemon/templatetags/pokemon_extras.py`)

### Bug 41 🔴 — Typo en template.Library()
- **Línea 3:** `template.Libary()` (falta la 'r')
- **Error:** `AttributeError: module 'django.template' has no attribute 'Libary'`
- **Fix:** `template.Library()`

### Bug 42 🟡 — Nombre de filtro no coincide
- **Línea 6:** filtro registrado como `'type_color'` pero en `pokemon_detail.html` se usa `pokemon_type_color`
- **Error:** `TemplateSyntaxError: Invalid filter: 'pokemon_type_color'`
- **Fix:** Cambiar en template `{{ type|pokemon_type_color }}` a `{{ type|type_color }}` O cambiar el name del registro

### Bug 43 🟢 — División por cero no manejada
- **Línea 38:** `value / total * 100` sin validar que `total` no sea 0
- **Error:** `ZeroDivisionError` al usar el filtro con total=0
- **Fix:** Agregar: `if total == 0: return 0`

---

## Templates

### Bug 44 🟢 — Falta `{% load static %}` en base.html
- **Archivo:** `base.html` línea 7
- **Error:** `TemplateSyntaxError: 'static' is not a registered tag library`
- **Fix:** Agregar `{% load static %}` al inicio del archivo

### Bug 45 🟢 — Block content no cerrado en base.html
- **Archivo:** `base.html` línea ~43
- **Error:** `{% block content %}` sin `{% endblock %}`
- **Fix:** Agregar `{% endblock %}` después del block content y antes de `</main>`

### Bug 46 🟢 — URL name en español
- **Archivo:** `pokemon_list.html` línea ~22
- **Error:** `{% url 'pokemon_detalle' ... %}` → `NoReverseMatch`
- **Fix:** Cambiar a `{% url 'pokemon_detail' pokemon.pk %}`

### Bug 47 🟡 — Falta llave de cierre en variable
- **Archivo:** `pokemon_list.html` línea ~29
- **Error:** `{{ pokemon.name }` → error de parseo en template
- **Fix:** `{{ pokemon.name }}`

### Bug 48 🟡 — endblock en vez de endfor
- **Archivo:** `pokemon_list.html` línea ~40
- **Error:** `{% endblock %}` cierra el for loop
- **Fix:** Cambiar `{% endblock %}` a `{% endfor %}`

### Bug 49 🟡 — Extends con typo
- **Archivo:** `search_results.html` línea 1
- **Error:** `{% extends "pokemon/bse.html" %}` → `TemplateDoesNotExist`
- **Fix:** `{% extends "pokemon/base.html" %}`

### Bug 50 🔴 — csrf_token fuera del form
- **Archivo:** `pokemon_form.html` línea ~13-14
- **Error:** `{% csrf_token %}` está antes de `<form>`, no dentro
- **Fix:** Mover `{% csrf_token %}` dentro del `<form method="post">`

### Bug 51 🔴 — Campo `pokemon.legendary` inexistente
- **Archivo:** `pokemon_detail.html` línea ~57
- **Error:** `{% if pokemon.legendary %}` → el campo es `is_legendary`
- **Fix:** `{% if pokemon.is_legendary %}`

### (CSS Bonus) Bug visual — Clase CSS no coincide
- **Archivo:** `pokemon_list.html` usa `class="pokemon-crd"` pero CSS define `.pokemon-card`
- **Error:** Cards sin estilos aplicados
- **Fix:** Cambiar `pokemon-crd` a `pokemon-card` en el template

---

## Orden sugerido de resolución

### Fase 1 — Hacer funcionar el servidor (~20 min)
Bugs: 1, 5, 6, 4, 16, 8, 9

### Fase 2 — Migraciones y modelos (~25 min)
Bugs: 10, 11, 12, 13, 14, 15

### Fase 3 — Templates base y navegación (~20 min)
Bugs: 44, 45, 7, 41, 42

### Fase 4 — Lista de Pokémon (~20 min)
Bugs: 17, 18, 46, 47, 48, CSS bonus

### Fase 5 — Detalle, búsqueda y CRUD (~25 min)
Bugs: 19, 20, 21, 22, 23, 49, 50, 51

### Fase 6 — Admin y funcionalidades avanzadas (~20 min)
Bugs: 36, 37, 38, 24, 25, 26

### Fase 7 — Context processors, forms y polish (~20 min)
Bugs: 39, 40, 31, 32, 33, 34, 35, 27, 28, 29, 30, 43, 3, 2

**Tiempo total estimado: ~2.5 a 3 horas**
