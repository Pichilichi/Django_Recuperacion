from django.db import models

class Usuario (models.Model):
    username = models.CharField(max_length=30)
    password = models.IntegerField()

class Especialista (models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_nac = models.DateTimeField()
    foto = models.CharField(max_length=100)
    biografia = models.CharField(max_length=255)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Cliente (models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fecha_nac = models.DateTimeField()
    foto = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Cita (models.Model):
    fecha_cita = models.DateTimeField()
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    id_especialista = models.ForeignKey(Especialista,on_delete=models.CASCADE)
    informe = models.TextField()
    realizada = models.BooleanField()

class Mensaje (models.Model):
    id_emisor = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name = "id_emisor")
    id_receptor = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name = "id_receptor")
    fecha_mensaje = models.DateTimeField()
    asunto = models.CharField(max_length=50)
    texto = models.TextField()
    leido = models.BooleanField()