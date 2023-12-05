from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import ModelUsuario, Treino, DescricaoTreino, Prova, Resultado
from django.utils import timezone

class ModelUsuarioTest(TestCase):

    def test_create_user(self):
        # Teste a criação de um usuário normal com todos os campos obrigatórios
        user = ModelUsuario.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            fone='11987654321',
            data_nascimento='1990-01-01',
            sexo='M',
            cpf='123.456.789-00',
            endereco='Rua Exemplo, 123',
            curso='Curso Exemplo',
            matricula='12345678',
            socio=True
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # Teste a criação de um superusuário
        superuser = ModelUsuario.objects.create_superuser(
            email='superuser@example.com',
            password='superpass123'
        )
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertTrue(superuser.check_password('superpass123'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_string_representation(self):
        # Teste o método __str__ do usuário
        user = ModelUsuario(email='testuser@example.com')
        self.assertEqual(str(user), 'testuser@example.com')

class TreinoTest(TestCase):

    def test_treino_creation(self):
        # Teste a criação de um treino
        treino = Treino.objects.create(descricao='Treino de Teste')
        self.assertEqual(treino.descricao, 'Treino de Teste')

class DescricaoTreinoTest(TestCase):

    def setUp(self):
        # Configuração para criar um treino e um usuário para o teste de descrição do treino
        self.treino = Treino.objects.create(descricao='Treino de Teste')
        self.usuario = ModelUsuario.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )

    def test_descricao_treino_creation(self):
        # Teste a criação de uma descrição de treino
        descricao_treino = DescricaoTreino.objects.create(
            treino=self.treino,
            modelusuario=self.usuario,
            PSE_treinador=5,
            PSE_atleta=4,
            presenca=True,
            data_treino=timezone.now().date(),
            distancia_total=1000
        )
        self.assertEqual(descricao_treino.treino, self.treino)
        self.assertEqual(descricao_treino.modelusuario, self.usuario)
        self.assertEqual(descricao_treino.PSE_treinador, 5)
        self.assertEqual(descricao_treino.PSE_atleta, 4)
        self.assertTrue(descricao_treino.presenca)

class ProvaTest(TestCase):

    def test_prova_creation(self):
        # Teste a criação de uma prova
        prova = Prova.objects.create(
            nome_prova='Prova de 100m',
            distancia=100.00,
            estilo='Livre',
            naipe='Masculino'
        )
        self.assertEqual(prova.nome_prova, 'Prova de 100m')
        self.assertEqual(prova.distancia, 100.00)
        self.assertEqual(prova.estilo, 'Livre')
        self.assertEqual(prova.naipe, 'Masculino')

class ResultadoTest(TestCase):

    def setUp(self):
        # Configuração para criar um usuário e uma prova para o teste de resultado
        self.usuario = ModelUsuario.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.prova = Prova.objects.create(
            nome_prova='Prova de 100m',
            distancia=100.00,
            estilo='Livre',
            naipe='Masculino'
        )

    def test_resultado_creation(self):
        # Teste a criação de um resultado
        resultado = Resultado.objects.create(
            modelusuario=self.usuario,
            prova=self.prova,
            tempo=timezone.timedelta(seconds=50),
            classificacao=1,
            data_prova=timezone.now().date()
        )
        self.assertEqual(resultado.modelusuario, self.usuario)
        self.assertEqual(resultado.prova, self.prova)
        self.assertEqual(resultado.tempo, timezone.timedelta(seconds=50))
        self.assertEqual(resultado.classificacao, 1)
