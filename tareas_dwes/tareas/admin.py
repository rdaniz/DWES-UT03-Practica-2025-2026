from django.contrib import admin

# Esto lo importa Django automáticamente, pero no funciona, en cambio del otro modo si
# from tareas_dwes.tareas.models import Tarea

from .models import Tarea

# Register your models here.
admin.site.register(Tarea)