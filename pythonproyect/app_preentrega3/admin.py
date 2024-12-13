from django.contrib import admin
from .models import Libro, Autor, Editorial, Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')
    list_filter = ('autor', 'fecha')
    search_fields = ('titulo', 'autor', 'cuerpo')
    date_hierarchy = 'fecha'

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicacion')
    list_filter = ('autor', 'publicacion')
    search_fields = ('titulo', 'autor')
    date_hierarchy = 'publicacion'

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'biografia')

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')




