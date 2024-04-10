from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.test import APIClient

from users.models import CustomUser

class GroupAPITestCaseWithPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        content_type = ContentType.objects.get_for_model(Group)
        permissions = Permission.objects.filter(content_type=content_type)
        self.user.user_permissions.set(permissions)
        self.client.force_authenticate(user=self.user)

    def test_group_list(self):
        Group.objects.create(name='Test Group')
        response = self.client.get('/api-users/groups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_group(self):
        data = {'name': 'New Group'}
        response = self.client.post('/api-users/groups/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get().name, 'New Group')

    def test_group_detail(self):
        group = Group.objects.create(name='Test Group')
        response = self.client.get(f'/api-users/groups/{group.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Group')

    def test_update_group(self):
        group = Group.objects.create(name='Test Group')
        data = {'name': 'Updated Group'}
        response = self.client.put(f'/api-users/groups/{group.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Group.objects.get().name, 'Updated Group')

    def test_partial_update_group(self):
        group = Group.objects.create(name='Test Group')
        data = {'name': 'Partial Update Group'}
        response = self.client.patch(f'/api-users/groups/{group.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Group.objects.get().name, 'Partial Update Group')

    def test_delete_group(self):
        group = Group.objects.create(name='Test Group')
        response = self.client.delete(f'/api-users/groups/{group.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Group.objects.count(), 0)

class GroupAPITestCaseWithOutPermission(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_group_list(self):
        Group.objects.create(name='Test Group')
        response = self.client.get('/api-users/groups/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_group(self):
        data = {'name': 'New Group'}
        response = self.client.post('/api-users/groups/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_detail(self):
        group = Group.objects.create(name='Test Group')
        response = self.client.get(f'/api-users/groups/{group.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_group(self):
        group = Group.objects.create(name='Test Group')
        data = {'name': 'Updated Group'}
        response = self.client.put(f'/api-users/groups/{group.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_group(self):
        group = Group.objects.create(name='Test Group')
        data = {'name': 'Partial Update Group'}
        response = self.client.patch(f'/api-users/groups/{group.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_group(self):
        group = Group.objects.create(name='Test Group')
        response = self.client.delete(f'/api-users/groups/{group.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)