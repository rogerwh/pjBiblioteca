from django.db import models


# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["nombre"]

    def __unicode__(self):
        return '{}'.format(self.nombre.decode('utf-8'))


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField('e-mail', blank=True)

    def __unicode__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return '%s-%s-%s.%s' %(instance.titulo, instance.fecha_publicacion, instance.editor, extension)


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to=upload_location)

    def __unicode__(self):
        return '{}'.format(self.titulo)