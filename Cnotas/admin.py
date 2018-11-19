from django.contrib import admin
from grados.models import Materia, MateriaAdmin, Grado, GradoAdmin

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
