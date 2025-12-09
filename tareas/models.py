import uuid
from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Identificador único")
    titulo = models.CharField(max_length=150, help_text="Nombre o tíutlo de la tarea")
    descripcion = models.TextField(help_text="Descripción detallada")
    completada = models.BooleanField(default=False, help_text="Estado de la tarea")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación")
    fecha_recordatorio = models.DateTimeField(help_text="Fecha recordatorio")

    def __str__(self):
        return self.titulo