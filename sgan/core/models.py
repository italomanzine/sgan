from django.db import models

#from django.utils import timezone # para models.DateTimeField

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    curso = models.CharField(max_length=30, blank=True, null=True)
    #senha = models.CharField(max_length=30)
    tipo_usuario = models.CharField(max_length=30)
    socio = models.BooleanField()
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    matricula = models.CharField(max_length=10, blank=True, null=True)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)


class Treino(models.Model):
    # Campos do modelo Treino
    descricao = models.CharField(max_length=1000, blank=True, null=True)


class DescricaoTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    PSE_treinador = models.DecimalField(max_digits=2, decimal_places=2)
    PSE_atleta = models.DecimalField(max_digits=2, decimal_places=2)
    presença = models.CharField(max_length=20)
    data_treino = models.DateField(blank=True, null=True)
    distancia_total = models.DecimalField(max_digits=7, decimal_places=2)

class Prova(models.Model):
    # Campos do modelo Prova (adapte de acordo com suas necessidades)
    nome_prova = models.CharField(max_length=50)
    distancia = models.DecimalField(max_digits=7, decimal_places=2)  
    estilo = models.CharField(max_length=25)
    naipe = models.CharField(max_length=20)
    
class Resultado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    # Outros campos específicos do relacionamento 'resultado'
    tempo = models.DurationField()# exemplo de armazenamento de dados "00:02:30", "01:30:45.000500" vai armazenando de "HH:MM:SS.ssssss" (horas, minutos, segundos e microssegundos).
    classificacao = models.PositiveIntegerField()  # Campo para armazenar a classificação como número inteiro
    data_prova = models.DateField()

