from __future__ import unicode_literals

from django.db import models
from apps.patients.models import *
from apps.therapists.models import *

class TherapySession(models.Model):
    date = models.DateField(verbose_name='Fecha')
    objective = models.CharField(max_length=128, verbose_name='Objetivo')
    description = models.CharField(max_length=1024, verbose_name='Descripción')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, verbose_name='Terapeuta')
    

    
class Movement(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Nombre')
    


class Minigame(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Nombre')
    description = models.CharField(max_length=1024, verbose_name='Descripción')
    movements = models.ManyToManyField(Movement, verbose_name='Movimientos')
    





class GameSession(models.Model):
    date = models.DateField(verbose_name='Fecha')
    score = models.IntegerField(verbose_name='Puntaje')
    repetitions = models.IntegerField(verbose_name='Repeticiones')
    time = models.IntegerField(verbose_name='Tiempo')
    level = models.IntegerField(verbose_name='Nivel')
    therapy = models.ForeignKey(TherapySession, on_delete=models.CASCADE, verbose_name='Terapeuta')
    minigame = models.ForeignKey(Minigame, on_delete=models.CASCADE, verbose_name='Minijuego')
    movements = models.ManyToManyField(Movement, through="Performance")
      
    
class Performance(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, verbose_name='Movimiento')
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE, verbose_name='Sesión de Juego')
    angle = models.IntegerField(verbose_name='Angulo')
    

    
    
    