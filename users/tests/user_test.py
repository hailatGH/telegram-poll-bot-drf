from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.test import APIClient

from users.models import CustomUser

class UserAPITestCaseWithPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        content_type = ContentType.objects.get_for_model(CustomUser)
        permissions = Permission.objects.filter(content_type=content_type)
        self.user.user_permissions.set(permissions)
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        response = self.client.get('/api-users/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user(self):
        data = {'username': 'testuser2', 'password': 'password'}
        response = self.client.post('/api-users/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_user_detail(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        response = self.client.get(f'/api-users/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser2')

    def test_update_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        data = {'username': 'testuser3', 'password': 'password'}
        response = self.client.put(f'/api-users/users/{user.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser3')

    def test_partial_update_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        data = {'username': 'testuser3'}
        response = self.client.patch(f'/api-users/users/{user.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser3')

    def test_delete_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        response = self.client.delete(f'/api-users/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class UserAPITestCaseWithOutPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        response = self.client.get('/api-users/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user(self):
        data = {'username': 'testuser2', 'password': 'password'}
        response = self.client.post('/api-users/users/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_detail(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        response = self.client.get(f'/api-users/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        data = {'username': 'testuser3', 'password': 'password'}
        response = self.client.put(f'/api-users/users/{user.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        data = {'username': 'testuser3'}
        response = self.client.patch(f'/api-users/users/{user.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user(self):
        user = CustomUser.objects.create(username='testuser2', password='password')
        response = self.client.delete(f'/api-users/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)