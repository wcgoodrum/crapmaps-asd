from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

# Create your tests here.
class AuthTests(TestCase):
    #https://stackoverflow.com/questions/19897225/django-unit-test-login-using-python-social-auth
    #user creation and setup 
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe',
            password='12345',
            is_active=True,
            is_staff=True,
            is_superuser=True
        ) 
        self.user.set_password('hello') 
        self.user.save()

    #response code of 200 for default page
    def test_response_status(self):
        self.client.force_login(self.user, "django.contrib.auth.backends.ModelBackend")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    #tests for page content
    # def test_response_content(self):
    #     self.client.force_login(self.user, "django.contrib.auth.backends.ModelBackend")
    #     response = self.client.get(reverse("crap_maps:index"))
    #     self.assertContains(response,
    #         "<p>Welcome John Doe. Your username is testuser</p>"
    #     )
    #     self.assertContains(response,
    #         "<p>You are not an admin.</p>"
    #     )
    
    def test_login_success(self):
        login = self.client.login(username='testuser', password='hello') 
        self.assertTrue(login)

    def test_login_fail(self):
        login = self.client.login(username='testuser', password='goodbye') 
        self.assertFalse(login)
