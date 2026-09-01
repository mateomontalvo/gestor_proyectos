from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proyecto


def home(request):
    return render(request, 'home.html')


def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})


def nuevos_registros(request):
    proyectos = [
        Proyecto(
            nombre="Aplicacion de biblioteca",
            descripcion="Aplicacion web para gestionar los libros y prestamos de la biblioteca",
            duracion=200
        ),
        Proyecto(
            nombre="Aplicacion de mensajeria",
            descripcion="Aplicacion web para enviar mensajes de texto",
            duracion=1000
        ),
        Proyecto(
            nombre="Tienda virtual",
            descripcion="Aplicacion web para comprar y vender productos en linea",
            duracion=200
        ),
    ]

    for p in proyectos:
        p.save()

    return HttpResponse("Registros guardados")


def ver_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, 'detalle-proyecto.html', {'proyecto': proyecto})


def nuevo_proyecto(request):
    return render(request, 'nuevo-proyecto.html')


def crear_proyecto(request):
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    duracion = request.POST.get('duracion')

    if nombre and descripcion and duracion:
        proyecto = Proyecto(
            nombre=nombre,
            descripcion=descripcion,
            duracion=int(duracion)
        )
        proyecto.save()
        return redirect('proyectos')

    return render(request, 'nuevo-proyecto.html')


def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')


def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)

    if request.method == 'POST':
        pass

    return render(request, 'editar-proyecto.html', {'proyecto': proyecto})


def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'crear-tarea.html', {'proyecto': proyecto})