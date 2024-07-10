# planets/management/commands/fetch_planets.py
import requests
from django.core.management.base import BaseCommand
from planets.models import Planet

class Command(BaseCommand):
    help = 'Fetch planets data from GraphQL API and store in the database'

    def handle(self, *args, **kwargs):
        url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'
        query = """
        query {
          allPlanets {
            planets {
              name
              population
              terrains
              climates
            }
          }
        }
        """
        response = requests.post(url, json={'query': query})
        data = response.json()

        for planet_data in data['data']['allPlanets']['planets']:
            print(planet_data)

            Planet.objects.update_or_create(
                name=planet_data['name'],
                defaults={
                    'population': planet_data['population'] or 'unknown',
                    'terrains': ', '.join(planet_data['terrains']) if planet_data['terrains'] else 'unknown',
                    'climates': ', '.join(planet_data['climates']) if planet_data['climates'] else 'unknown',
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored planets data'))
