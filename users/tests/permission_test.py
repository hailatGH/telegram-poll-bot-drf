from django.test import TestCase
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.test import APIClient

from users.models import CustomUser

class PermissionAPITestCaseWithPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        content_type = ContentType.objects.get_for_model(Permission)
        permissions = Permission.objects.filter(content_type=content_type)
        self.user.user_permissions.set(permissions)
        self.client.force_authenticate(user=self.user)

    def test_permission_list(self):
        response = self.client.get('/api-users/permissions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Permission.objects.count())

class PermissionAPITestCaseWithOutPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_permission_list(self):
        response = self.client.get('/api-users/permissions/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)