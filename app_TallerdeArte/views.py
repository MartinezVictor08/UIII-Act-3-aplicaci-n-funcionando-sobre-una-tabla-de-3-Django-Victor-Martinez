from django.shortcuts import render, redirect
from .models import Instructor

# Página de inicio
def inicio_TallerdeArte(request):
    return render(request, 'inicio.html')


# Agregar instructor
def agregar_instructor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        experiencia_anios = request.POST['experiencia_anios']
        sueldo = request.POST['sueldo']

        nuevo = Instructor(
            nombre=nombre,
            apellido=apellido,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo,
            experiencia_anios=experiencia_anios,
            sueldo=sueldo
        )
        nuevo.save()
        return redirect('ver_instructor')
    return render(request, 'instructor/agregar_instructor.html')


# Ver instructores
def ver_instructor(request):
    instructores = Instructor.objects.all()
    return render(request, 'instructor/ver_instructor.html', {'instructores': instructores})


# Actualizar instructor
def actualizar_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    return render(request, 'instructor/actualizar_instructor.html', {'instructor': instructor})


# Realizar actualización
def realizar_actualizacion_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    if request.method == 'POST':
        instructor.nombre = request.POST['nombre']
        instructor.apellido = request.POST['apellido']
        instructor.especialidad = request.POST['especialidad']
        instructor.telefono = request.POST['telefono']
        instructor.correo = request.POST['correo']
        instructor.experiencia_anios = request.POST['experiencia_anios']
        instructor.sueldo = request.POST['sueldo']
        instructor.save()
        return redirect('ver_instructor')
    return redirect('ver_instructor')


# Borrar instructor
def borrar_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    instructor.delete()
    return redirect('ver_instructor')