from django import forms
from .models import Pokemon, Trainer


class TrainerForm(forms.Form):
    class Meta:
        model = Trainer
        fields = ['name', 'badge_count']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del entrenador',
            }),
        }


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all_'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Pokémon',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'pokedex_number': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return description

    def clean_hp(self):
        hp = self.cleaned_data.get('hp')
        if hp is not None and hp < 0:
            raise ValueError("HP no puede ser negativo")
        if hp is not None and hp > 999:
            raise ValueError("HP no puede ser mayor a 999")
        return hp


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar Pokémon...',
        }),
    )
