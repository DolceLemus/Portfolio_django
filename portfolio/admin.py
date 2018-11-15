from django.contrib import admin
from .models import Project

# Register your models here.

# clase para extender las funcionalidades del panel del admin y sirve para mostrar los campos en el admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 


admin.site.register(Project, ProjectAdmin)
