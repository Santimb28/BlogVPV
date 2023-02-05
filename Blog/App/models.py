from django.db import models
from django.contrib.auth.models import User


class Ropa(models.Model):
    Prendas = (
        ('camisas','Camisas'),
        ('zapatos','Zapatos'),
        ('pantalones','Pantalones'),
        ('boxer','Boxer'),
        ('pulseras','Pulseras'),
        ('gorras', 'Gorras'),
        ('hoodies', 'Hoodies')
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    prenda = models.CharField(max_length=15, choices=Prendas, default='hoodies')
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contactoTLF = models.IntegerField()
    email_contacto = models.EmailField()
    imagenPrenda = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fecha_publicacion']

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    comentario = models.ForeignKey(Ropa, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)