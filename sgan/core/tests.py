from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

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
