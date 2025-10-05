from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login(self):
        User.objects.create_user(username='testuser', password='password123')
        login = self.client.login(username='testuser', password='password123')
        self.assertTrue(login)

    def test_logout(self):
        User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect usually after logout

    def test_profile_update(self):
        # Create user and force login
        user = User.objects.create_user(username='user1', password='pass123')
        self.client.force_login(user)

        response = self.client.post(reverse('profile'), {
            'username': 'user1updated',
            'email': 'updated@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        user.refresh_from_db()
        self.assertEqual(user.username, 'user1updated')
        self.assertEqual(user.email, 'updated@example.com')
