from django.db import models
from django.contrib.auth.models import User

class Therapist(User):


    
    name = models.CharField(max_length=64, verbose_name='Nombre')
    lastname = models.CharField(max_length=64, verbose_name='Apellido')
    id_type = models.CharField(max_length=64,  verbose_name='Tipo de identificación')
    genre = models.CharField(max_length=64, verbose_name='Género')
    
    def __unicode__(self):
        return self.name + " " + self.lastname