from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auto(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=255, blank=False, null=False)
    modelo = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=False)
    ano = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to='image/posts', max_length=255, blank=False, null= False)
    precio = models.FloatField(blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)

    @property
    def only_year(self):
        return self.ano.strftime('%Y')

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'
        ordering = ['id']
        indexes = [
            models.Index(fields=['marca', 'modelo', 'slug', 'ano', 'status'])
        ]

    def __str__(self):
        return self.modelo

class Comment(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']
        indexes = [
            models.Index(fields=['user', 'auto', 'date', 'status'])
        ]

    def __str__(self):
        return f'{self.auto.modelo} - {self.user.username}'

class Alquiler(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    date_start = models.DateField(blank=False, null=False)
    date_end = models.DateField(blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquilers'
        ordering = ['id']
        indexes = [
            models.Index(fields=['user', 'auto', 'date_start', 'date_end','status'])
        ]

    def __str__(self):
        return f'{self.auto.modelo} - {self.user.username}'