from django.db import models
from django.contrib.auth.models import User
from .models import Suscripciones


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='equipo/')
    cargo = models.CharField(max_length=100)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Suscripciones(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.TextField(verbose_name="descripcion",null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Suscripciones(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    # Otros campos relevantes para representar una revista

    def __str__(self):
        return self.titulo
    

class Revista(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    # Otros campos relevantes

class CarroItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    # Otros campos relevantes