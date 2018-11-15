from django.db import models

# Create your models here.

class Project (models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to = "projects")
    # Fecha de creacion,  auto_now_add=True | se creará la fecha al crearlo por primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # Fecha de modificacion
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        # mas nuevo a mas antiguo
        ordering = ["-created"]
    
    def __str__(self):
        return self.title