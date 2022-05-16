import re
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from memory.models import Memory


class MemoryModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.memory = Memory.objects.create(
            user=self.user,
            name='Test Memory',
            species='Test Species',
            weight=1.0,
            length=1.0,
            latitude=1.0,
            longitude=1.0,
            description='Test Description',
            photo='Test Photo'
        )

    def test_memory_creation(self):
        self.assertEqual(self.memory.name, 'Test Memory')
        self.assertEqual(self.memory.species, 'Test Species')
        self.assertEqual(self.memory.weight, 1.0)
        self.assertEqual(self.memory.length, 1.0)
        self.assertEqual(self.memory.latitude, 1.0)
        self.assertEqual(self.memory.longitude, 1.0)
        self.assertEqual(self.memory.description, 'Test Description')
        self.assertEqual(self.memory.photo, 'Test Photo')

    def test_memory_str(self):
        self.assertEqual(str(self.memory), 'Test Memory')


class MemoryListViewTest(TestCase):
    
        def setUp(self):
            self.user = User.objects.create_user(
                username='testuser',
                password='12345'
            )
            self.memory = Memory.objects.create(
                user=self.user,
                name='Test Memory',
                species='Test Species',
                weight=1.0,
                length=1.0,
                latitude=1.0,
                longitude=1.0,
                description='Test Description',
                photo='Test Photo'
            )
    
        def test_memory_list_view(self):
            response = self.client.get(reverse('latest-memories'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Test Memory')


class MemoryTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='vineetrawat',
            password='100barlol'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_memory(self):

        url = reverse('create-memory')
        data = {
            'name': 'Test Memory',
            'species': 'Test Species',
            'weight': 1.0,
            'length': 1.0,
            'latitude': 1.0,
            'longitude': 1.0,
            'description': 'Test Description',
            'photo': 'Test Photo'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Memory.objects.count(), 1)
        self.assertEqual(Memory.objects.get().name, 'Test Memory')
        return response
