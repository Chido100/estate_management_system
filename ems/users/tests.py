from django.test import TestCase
from .models import User
from django.core import mail
from django.urls import reverse



class RegsiterLoginResidentTest(TestCase):
    def test_user_registration(self):
        # User registration data
        username = 'tester1'
        email = 'testuser@email.com'
        password = 'Password123'

        # Simulate user registration
        response = self.client.post(reverse('register-resident'), {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password,
        })

        # Check registration was successful
        self.assertEqual(response.status_code, 302)

    
    def test_all_users(self):
        users = User.objects.all()
        number_of_users = len(users)
        print(number_of_users)
        self.assertEqual(number_of_users, 0)



