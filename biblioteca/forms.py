from django import forms
from biblioteca.models import Autor, Editor, Libro


class EditorForm(forms.ModelForm):

    class Meta:
        model = Editor

        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',
        ]
        labels = {
            'nombre': 'Nombre completo',
            'domicilio': 'Domicilio',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'Pais',
            'website': 'Pagina Web',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor

        fields = [
            'nombre',
            'apellidos',
            'email',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Correo electronico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
        }


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]
        labels = {
            'titulo': 'Titulo del libro',
            'autores': 'Autores',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha de publicacion',
            'portada': 'Portada',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.CheckboxSelectMultiple(),
            'editor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control'}),
        }