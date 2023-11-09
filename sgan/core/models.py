from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.core.validators import RegexValidator #para o atributo fone, cpf 

# Define um validador personalizado para aceitar apenas dígitos e ter 11 caracteres
phone_validator = RegexValidator(
    regex=r'^\d{11}$',
    message="O número de celular deve conter exatamente 11 dígitos.",
)
# Define um validador para o formato de CPF (xxx.xxx.xxx-xx)
cpf_validator = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="O CPF deve estar no formato xxx.xxx.xxx-xx",
)
# Define um validador para o formato de MATRICULA (xxxxxxxx)
matricula_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Informe sua matrícula com 8 dígitos.",
)

### para as configurações BD do admin do django
class UsuarioManager(BaseUserManager):
    use_in_migrations=True
    #informamos que esse vai ser o model de user que vamos usar no BD para autentificação

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # nos campos que vierem no **extra_fields, podemos garantir que o campo 'is_superuser' seja falso.
        extra_fields.setdefault('is_superuser', False)
        # nos campos que vierem no **extra_fields, podemos garantir que o campo 'is_staff' seja verdadeiro.
        # extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuário precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuário precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)
#


class ModelUsuario(AbstractUser):
    email=models.EmailField('E-mail', unique=True) # usar email para fazer o login
    fone=models.CharField(
        max_length=11,
        validators=[phone_validator],
        blank=True,
        verbose_name="Número de celular",
        help_text="Somente números (DDD + 9 dígitos)",
    )
    is_staff=models.BooleanField('Treinador', default=True)
    #meus incrmentos 31/10/2023
    data_nascimento = models.DateField(null=True)
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        verbose_name="Sexo",
        help_text="Selecione o sexo: Feminino, Masculino ou Outros",
    )
    cpf = models.CharField(
        max_length=14,  # Com traços e pontos, o máximo é 14 caracteres
        unique=True,
        validators=[cpf_validator],
        verbose_name="CPF",
        help_text="Informe seu CPF no formato xxx.xxx.xxx-xx",
    )
    endereco = models.CharField(max_length=100)
    
    curso = models.CharField(max_length=100)
    #curso = models.CharField(max_length=100, blank=True, verbose_name="Curso")


    matricula =models.CharField(
        max_length=8,
        unique=True,
        blank=True, 
        null=True,
        validators=[matricula_validator],
        verbose_name="Matrícula",
        help_text="Informe sua matrícula com 8 dígitos.",
    )
    
    socio = models.BooleanField('Sócio do Grêmio Fronteira', default=True)
    

     

    USERNAME_FIELD='email'      #poderiamos definir qualquer outro campo como username
    REQUIRED_FIELDS=['first_name', 'last_name', 'fone','data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio']
    #campos email e senha não precisa informar, pois o Django sabe que eles são obrigatorios para a estrutura 

    def __str__(self):
        return self.email

    objects = UsuarioManager()#com isso especificicamos parao django usar o noss manager e não o padrao
    

#Demais tabelas 
"""
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
"""

class Treino(models.Model):
    # Campos do modelo Treino
    descricao = models.CharField(max_length=1000)


class DescricaoTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    modelusuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    PSE_treinador = models.DecimalField(max_digits=2, decimal_places=2)
    PSE_atleta = models.DecimalField(max_digits=2, decimal_places=2)
    presença = models.BooleanField()
    data_treino = models.DateField()
    distancia_total = models.DecimalField(max_digits=7, decimal_places=2)

class Prova(models.Model):
    # Campos do modelo Prova (adapte de acordo com suas necessidades)
    nome_prova = models.CharField(max_length=50)
    distancia = models.DecimalField(max_digits=7, decimal_places=2)  
    estilo = models.CharField(max_length=25)
    naipe = models.CharField(max_length=20)
    
class Resultado(models.Model):
    modelusuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    # Outros campos específicos do relacionamento 'resultado'
    tempo = models.DurationField()# exemplo de armazenamento de dados "00:02:30", "01:30:45.000500" vai armazenando de "HH:MM:SS.ssssss" (horas, minutos, segundos e microssegundos).
    classificacao = models.PositiveIntegerField()  # Campo para armazenar a classificação como número inteiro
    data_prova = models.DateField()


