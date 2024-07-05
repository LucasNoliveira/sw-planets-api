from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Planet

class PlanetAPITest(APITestCase):
    """
    Test cases for CRUD operations on Planet model via API endpoints.
    """

    def setUp(self):
        """
        Sets up initial data for each test method.
        """
        super().setUp()
        self.tatooine = Planet.objects.create(
            name="Tatooine",
            population="200000",
            terrains="desert",
            climates="arid"
        )
        self.hoth = Planet.objects.create(
            name="Hoth",
            population="unknown",
            terrains="ice",
            climates="frozen"
        )

    def test_create_planet(self):
        """
        Tests creation of a new planet via POST request.
        Asserts that the response status code is 201 (Created).
        Asserts that the number of Planet objects is 3 after creation.
        Asserts that a specific planet (Alderaan) exists in the database.
        """
        url = reverse('planet-list')
        data = {
            "name": "Alderaan",
            "population": "2000000000",
            "terrains": "grasslands, mountains",
            "climates": "temperate"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Planet.objects.count(), 3)
        self.assertEqual(Planet.objects.get(name="Alderaan").name, 'Alderaan')

    def test_get_planet(self):
        """
        Tests retrieving a specific planet (Tatooine) via GET request.
        Asserts that the response status code is 200 (OK).
        Asserts that the retrieved planet's name matches the expected name.
        """
        url = reverse('planet-detail', args=[self.tatooine.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.tatooine.name)

    def test_update_planet(self):
        """
        Tests updating a specific planet (Tatooine) via PUT request.
        Asserts that the response status code is 200 (OK).
        Asserts that the updated planet's population matches the expected value.
        """
        url = reverse('planet-detail', args=[self.tatooine.id])
        data = {
            "name": "Tatooine",
            "population": "300000",
            "terrains": "desert",
            "climates": "arid"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        updated_planet = Planet.objects.get(id=self.tatooine.id)
        self.assertEqual(updated_planet.population, "300000")

    def test_delete_planet(self):
        """
        Tests deleting a specific planet (Tatooine) via DELETE request.
        Asserts that the response status code is 204 (No Content).
        Asserts that the planet no longer exists in the database after deletion.
        """
        url = reverse('planet-detail', args=[self.tatooine.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Planet.objects.filter(id=self.tatooine.id).exists())
