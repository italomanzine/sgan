from datetime import timedelta
from django.test import TestCase
from core.forms import (
    ModelUsuarioCreateForm, 
    CustomAuthenticationForm, 
    TreinoForm, 
    DescricaoTreinoForm,
    ProvaForm, 
    ResultadoForm
)
from model_mommy import mommy

from sgan.core.models import Treino

class ModelUsuarioCreateFormTest(TestCase):
    def test_form_save_method(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'fone': '11987654321',
            'data_nascimento': '2000-01-01',
            'sexo': 'M',
            'cpf': '123.456.789-09',
            'endereco': 'Rua Teste',
            'curso': 'Teste Curso',
            'matricula': '12345678',
            'socio': True
        }
        form = ModelUsuarioCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsNotNone(user.pk)

class CustomAuthenticationFormTest(TestCase):
    def test_clean_username(self):
        user = mommy.make('myapp.ModelUsuario', email='test@example.com')
        form_data = {
            'username': 'Test@Example.com',  # Test email normalization
            'password': 'password'
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid())
        cleaned_username = form.clean_username()
        self.assertEqual(cleaned_username, user.email.lower())

class TreinoFormTest(TestCase):
    def test_form_meta(self):
        form = TreinoForm()
        self.assertEqual(form._meta.model, Treino)
        self.assertEqual(form._meta.fields, ['descricao'])

class DescricaoTreinoFormTest(TestCase):
    def test_form_exclude_treino_field(self):
        form = DescricaoTreinoForm()
        self.assertNotIn('treino', form.fields)

class ProvaFormTest(TestCase):
    def test_form_save(self):
        prova_data = {
            'nome_prova': '100m Livre',
            'distancia': '100.00',
            'estilo': 'Livre',
            'naipe': 'Masculino'
        }
        form = ProvaForm(data=prova_data)
        self.assertTrue(form.is_valid())
        prova = form.save()
        self.assertIsNotNone(prova.pk)

class ResultadoFormTest(TestCase):
    def test_clean_tempo(self):
        form_data = {
            'modelusuario': mommy.make('myapp.ModelUsuario').pk,
            'prova': mommy.make('myapp.Prova').pk,
            'tempo': '00:01:30.0',
            'classificacao': 1,
            'data_prova': '2023-01-01'
        }
        form = ResultadoForm(data=form_data)
        self.assertTrue(form.is_valid())
        tempo = form.clean_tempo()
        self.assertIsInstance(tempo, timedelta)

    def test_form_save(self):
        form_data = {
            'modelusuario': mommy.make('myapp.ModelUsuario').pk,
            'prova': mommy.make('myapp.Prova').pk,
            'tempo': '00:01:30.0',
            'classificacao': 1,
            'data_prova': '2023-01-01'
        }
        form = ResultadoForm(data=form_data)
        self.assertTrue(form.is_valid())
        resultado = form.save()
        self.assertIsNotNone(resultado.pk)
