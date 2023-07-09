from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

class CanalDe_Negocio(models.Model):
    nombreCanal= models.CharField(max_length=30)
    region= models.CharField(max_length=20)

class Persona_aCargo(models.Model):
    nombrePersona= models.CharField(max_length=30)   
    apellidoPersona= models.CharField(max_length=30)
    IDPersona= models.IntegerField()  

class Cliente_conDeuda(models.Model):
    nombre= models.CharField(max_length=30)
    deuda= models.BooleanField()
    montoDeuda= models.IntegerField()     


     