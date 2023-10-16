from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    curso = models.CharField(max_length=30, blank=True, null=True)
    senha = models.CharField(max_length=30)
    tipo_usuario = models.CharField(max_length=30)
    socio = models.BooleanField()
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    matricula = models.CharField(max_length=10, blank=True, null=True)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
