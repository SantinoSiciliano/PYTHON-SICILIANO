from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.titulo





