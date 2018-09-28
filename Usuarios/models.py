from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellidoPaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    email=models.EmailField()
    usuario=models.CharField(max_length=50,primary_key=True)
    domicilio=models.TextField()
