from django.shortcuts import render
from django.contrib import messages
from .forms import GradoForm
from Cnotas.models import Grado, Asignacion

def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], semestre = formulario.cleaned_data['semestre'], seccion = formulario.cleaned_data['seccion'], jornada = formulario.cleaned_data['jornada'], anio = formulario.cleaned_data['anio'])
            for materia_id in request.POST.getlist('materias'):
                asignacion= Asignacion(materia_id=materia_id, grado_id = grado.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Grado Guardado Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'Cnotas/grado_editar.html', {'formulario': formulario})
