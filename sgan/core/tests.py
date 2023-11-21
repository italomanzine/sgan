from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Treino

# testes automatizados para o login
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        User = get_user_model()
        self.user = User.objects.create_user(email='test@example.com', password='testpassword123')

    def test_login_page_status_code(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'test@example.com',  
            'password': 'testpassword123'
        }, follow=True)
        self.assertRedirects(response, reverse('index'), status_code=302, target_status_code=200)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'test@example.com',  
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_login_with_invalid_form(self):
        response = self.client.post(self.login_url, {
            'username': 'invalidemail',  
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_login_redirects_already_logged_in_user(self):
        self.client.login(email='test@example.com', password='testpassword123')  # Log in the user
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 302)  # Should redirect already logged in user
        self.assertTrue(response.url.startswith(reverse('index')))  # Check if redirect URL is index

    def tearDown(self):
        self.user.delete()

# testes automatizados para o treinos
class TreinosTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criar dados de teste que serão usados em todos os testes
        User = get_user_model()
        cls.staff_user = User.objects.create_user(
            email='staff@example.com',
            password='testpassword123',
            is_staff=True,
            cpf='12345678901'
        )
        cls.regular_user = User.objects.create_user(
            email='user@example.com',
            password='testpassword123',
            cpf='10987654321'
        )
        cls.treinos_url = reverse('treinos')
        
    def test_treinos_page_status_code_for_staff(self):
        self.client.login(email='staff@example.com', password='testpassword123')
        response = self.client.get(self.treinos_url)
        self.assertEqual(response.status_code, 200)

    def test_treinos_page_status_code_for_regular_user(self):
        self.client.login(email='user@example.com', password='testpassword123')
        response = self.client.get(self.treinos_url)
        self.assertEqual(response.status_code, 200)

    def test_create_treino_button_visible_for_staff(self):
        self.client.login(email='staff@example.com', password='testpassword123')
        response = self.client.get(self.treinos_url)
        self.assertContains(response, 'Criar Treino')

    def test_create_treino_button_not_visible_for_regular_user(self):
        self.client.login(email='user@example.com', password='testpassword123')
        response = self.client.get(self.treinos_url)
        self.assertNotContains(response, 'Criar Treino')

    def test_create_treino_modal_form(self):
        self.client.login(email='staff@example.com', password='testpassword123')
        response = self.client.post(reverse('create_treino'), data={
            'descricao': 'Teste de Treino',
            'data_treino': '2023-01-01',
            'PSE_treinador': '5',
            # ... other form fields ...
        })
        # Check if the treino was created
        self.assertEqual(Treino.objects.count(), 1)
        self.assertEqual(Treino.objects.first().descricao, 'Teste de Treino')

    def tearDown(self):
        if self.staff_user.id is not None:
            self.staff_user.delete()
        if self.regular_user.id is not None:
            self.regular_user.delete()