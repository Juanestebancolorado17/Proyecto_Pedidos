from django.db import models

class Informacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=20)
    edad = models.IntegerField()
    imagen_sujeto = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'informacion'
        verbose_name_plural = 'informaciones'

    def __str__(self):
        return self.nombre
    