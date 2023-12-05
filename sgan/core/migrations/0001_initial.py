# Generated by Django 4.2 on 2023-12-02 01:37

import core.models
from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('fone', models.CharField(blank=True, help_text='Somente números (DDD + 9 dígitos)', max_length=11, validators=[django.core.validators.RegexValidator(message='O número de celular deve conter exatamente 11 dígitos.', regex='^\\d{11}$')], verbose_name='Número de celular')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Treinador')),
                ('data_nascimento', models.DateField(null=True)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], help_text='Selecione o sexo: Feminino, Masculino ou Outros', max_length=1, verbose_name='Sexo')),
                ('cpf', models.CharField(help_text='Informe seu CPF no formato xxx.xxx.xxx-xx', max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='O CPF deve estar no formato xxx.xxx.xxx-xx', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')], verbose_name='CPF')),
                ('endereco', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('matricula', models.CharField(blank=True, help_text='Informe sua matrícula com 8 dígitos.', max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Informe sua matrícula com 8 dígitos.', regex='^\\d{8}$')], verbose_name='Matrícula')),
                ('socio', models.BooleanField(default=True, verbose_name='Sócio do Grêmio Fronteira')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prova', models.CharField(max_length=50)),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=7)),
                ('estilo', models.CharField(max_length=25)),
                ('naipe', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo', models.DurationField()),
                ('classificacao', models.PositiveIntegerField()),
                ('data_prova', models.DateField()),
                ('modelusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.prova')),
            ],
        ),
        migrations.CreateModel(
            name='DescricaoTreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PSE_treinador', models.DecimalField(decimal_places=2, max_digits=2)),
                ('PSE_atleta', models.DecimalField(decimal_places=2, max_digits=2)),
                ('presenca', models.BooleanField()),
                ('data_treino', models.DateField()),
                ('distancia_total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('modelusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.treino')),
            ],
        ),
    ]
