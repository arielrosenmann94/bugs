# 🐛 Pokédex — Práctica de Debugging

Tienes frente a ti una aplicación Django con errores. Tu misión es hacerla funcionar.

---

## ⚙️ Instalación

```bash
# 1. Clonar o descargar el proyecto y entrar a la carpeta
cd pokedex_project

# 2. Crear entorno virtual
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## 🔐 Configurar variables de entorno

El archivo `.env` no se comparte. Debes crearlo tú. Es simple:

```bash
# Crea el archivo
cp .env.example .env
```

Abre el `.env` y completa el valor de `SECRET_KEY`. Genérala en terminal:

```bash
# Linux / Mac / Git Bash
python -c "from django.core.signing import get_cookie_signer; import django; django.setup()" 2>/dev/null || python -c "import secrets; print('django-insecure-' + secrets.token_urlsafe(40))"
```

Copia el resultado y pégalo en `.env`:

```
SECRET_KEY=django-insecure-<lo-que-generaste>
DEBUG=True
ALLOWED_HOSTS=*
```

---

## ▶️ Primeros pasos

1. **Servidor**: Corre `python manage.py runserver` y mira qué pasa.
2. **Base de Datos**: Para ver datos en la app, deberás lograr que las migraciones funcionen y luego ejecutar:
   ```bash
   python manage.py seed_pokemon
   ```
   *(Esto cargará 20 Pokémon de ejemplo si todo está bien configurado).*

---

## 🎯 Objetivo

Lograr que la aplicación funcione completamente:
- Ver la lista de Pokémon
- Ver el detalle de cada uno
- Buscar por nombre
- Crear, editar y eliminar Pokémon
- Ver entrenadores
- Marcar favoritos

---

## 💡 Comandos útiles

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py seed_pokemon
python manage.py createsuperuser
```

---

## 🚨 IMPORTANTE — `BUGS_INSTRUCTOR.md`

Existe un archivo llamado `BUGS_INSTRUCTOR.md` que contiene la lista completa de todos los errores con sus soluciones. **NO LO LEAN BAJO NINGUNA CIRCUNSTANCIA** mientras trabajan en la práctica. El objetivo es que ustedes encuentren y resuelvan cada bug por su cuenta (con ayuda de IA como copiloto).

Este archivo será revisado **al final** de la práctica junto al instructor para verificar cuántos bugs lograron encontrar y corregir.

> Si lo leen antes de terminar, pierden toda la experiencia de aprendizaje. Confíen en el proceso. 🧠
