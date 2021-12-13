#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from biblioteca.models import Editor, Autor, Libro
from biblioteca.forms import EditorForm, AutorForm, LibroForm


# 0 Create your views here.
def index_biblioteca(request):
    #return HttpResponse("Holi, bienvenido a %s" % request.path)
    return render(request, 'biblioteca/index.html')


# con Funciones
def editor_create(request):
    form = EditorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('biblioteca:editor_listarfuncion')
    else:
        form = EditorForm()
    return render(request, 'biblioteca/editor_form.html', {'form': form})


def editor_list(request):
    editor = Editor.objects.all()
    contexto = {'editores': editor}
    return render(request, 'biblioteca/editor_list.html', contexto)


def editor_detail(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    return render(request, 'biblioteca/editor_detail.html', {'object':editor})


def editor_edit(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'GET':
        form = EditorForm(instance=editor)
    else:
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:editor_listarfuncion')
    return render(request, 'biblioteca/editor_form.html', {'form':form})


def editor_delete(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        editor.delete()
        return redirect('biblioteca:editor_listarfuncion')
    return render(request, 'biblioteca/editor_delete.html', {'object':editor})


def autor_create(request):
    form = AutorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('biblioteca:autor_listarfuncion')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/autor_form.html', {'form':form})


def autor_list(request):
    autor = Autor.objects.all()
    contexto = {'autores': autor}
    return render(request, 'biblioteca/autor_list.html', contexto)


def autor_detail(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    return render(request, 'biblioteca/autor_detail.html', {'object':autor})


def autor_edit(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'GET':
        form = AutorForm(instance=autor)
    else:
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:autor_listarfuncion')
    return render(request, 'biblioteca/autor_form.html', {'form':form})


def autor_delete(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        autor.delete()
        return redirect('biblioteca:autor_listarfuncion')
    return render(request, 'biblioteca/autor_delete.html', {'object':autor})


def libro_create(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('biblioteca:libro_listarfuncion')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/libro_form.html', {'form': form})


def libro_list(request):
    libro = Libro.objects.all()
    contexto = {'libros': libro}
    return render(request, 'biblioteca/libro_list.html', contexto)


def libro_detail(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    return render(request, 'biblioteca/libro_detail.html', {'object':libro})


def libro_edit(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:libro_listarfuncion')
    return render(request, 'biblioteca/libro_form.html', {'form':form})


def libro_delete(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect('biblioteca:libro_listarfuncion')
    return render(request, 'biblioteca/libro_delete.html', {'object':libro})


# con clases
class EditorCreate(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'biblioteca/editor_form.html'
    success_url = reverse_lazy('biblioteca:editor_listarclase')


class EditorList(ListView):
    model = Editor
    template_name = 'biblioteca/editor_list.html'


class EditorDetail(DetailView):
    model = Editor
    template_name = 'biblioteca/editor_detail.html'


class EditorUpdate(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = 'biblioteca/editor_form.html'
    success_url = reverse_lazy('biblioteca:editor_listarclase')


class EditorDelete(DeleteView):
    model = Editor
    template_name = 'biblioteca/editor_delete.html'
    success_url = reverse_lazy('biblioteca:editor_listarclase')


class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_listarclase')


class AutorList(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'


class AutorDetail(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'


class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_listarclase')


class AutorDelete(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_delete.html'
    success_url = reverse_lazy('biblioteca:autor_listarclase')


class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_listarclase')


class LbroList(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'


class LibroDetail(DetailView):
    model = Libro
    template_name = 'biblioteca/libro_detail.html'


class LbroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_listarclase')


class LibroDelete(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_delete.html'
    success_url = reverse_lazy('biblioteca:libro_listarclase')