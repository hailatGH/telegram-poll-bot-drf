from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import CustomGroup
from users.models import CustomUser as User

class GroupViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', password='password123')
        self.group_data = {'name': 'Test Group'}

    def test_create_group(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('group-list'), self.group_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomGroup.objects.count(), 1)
        self.assertEqual(CustomGroup.objects.get().name, 'Test Group')

    def test_update_group(self):
        group = CustomGroup.objects.create(name='Old Name')
        self.client.force_authenticate(user=self.user)
        updated_data = {'name': 'New Name'}
        response = self.client.put(reverse('group-detail', args=[group.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomGroup.objects.get().name, 'New Name')

    def test_retrieve_group(self):
        group = CustomGroup.objects.create(name='Test Group')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('group-detail', args=[group.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Group')

    def test_list_groups(self):
        CustomGroup.objects.create(name='Group 1')
        CustomGroup.objects.create(name='Group 2')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('group-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_destroy_group(self):
        group = CustomGroup.objects.create(name='Test Group')
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('group-detail', args=[group.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomGroup.objects.count(), 0)
