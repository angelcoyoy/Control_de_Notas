from django.contrib import admin
from Cnotas.models import Materia, MateriaAdmin, Grado, GradoAdmin

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
