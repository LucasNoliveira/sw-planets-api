from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    terrains = models.CharField(max_length=100)
    climates = models.CharField(max_length=100)

    def __str__(self):
        return self.name