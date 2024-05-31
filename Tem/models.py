from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to="Timjg/imagen")  # Crea carpeta y la guarda  en imagen
    url = URLField(blank=True)
