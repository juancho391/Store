from django.db import models

class Producto(models.Model):
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    image = models.ImageField(upload_to='store/images')
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=200)
    video = models.FileField(blank=True, upload_to='store/videos')



