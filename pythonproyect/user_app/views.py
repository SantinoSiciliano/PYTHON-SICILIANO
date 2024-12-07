from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Editorial, Blog
from .forms import LibroForm, AutorForm, EditorialForm, BlogForm, BusquedaForm

def home(request):
    return render(request, 'home.html')

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('home')
    return render(request, 'eliminar_libro.html', {'libro': libro})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditorialForm()
    return render(request, 'agregar_editorial.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            libros = Libro.objects.filter(titulo__icontains=termino)
            return render(request, 'resultados_busqueda.html', {'libros': libros})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

def agregar_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_blogs')
    else:
        form = BlogForm()
    return render(request, 'agregar_blog.html', {'form': form})

def editar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('listar_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'editar_blog.html', {'form': form})

def eliminar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('listar_blogs')
    return render(request, 'eliminar_blog.html', {'blog': blog})

def listar_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'listar_blogs.html', {'blogs': blogs})



