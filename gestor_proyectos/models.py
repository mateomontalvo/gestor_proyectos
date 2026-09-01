from django.db import models

class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100)  # Campo de texto (varchar)
    descripcion = models.TextField()  # Campo de texto largo
    duracion = models.IntegerField()  # Campo numérico entero

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    '''
    Modelo que representa una tarea
    '''

    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADA', 'Completada'),
    ]

    # Relación 1 a muchos: un Proyecto tiene muchas tareas
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='tareas')

    titulo = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Media')
    estado = models.CharField(max_length=11, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return self.titulo