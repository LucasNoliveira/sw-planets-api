from django.db import models

class Planet(models.Model):
    # Fields for Planet model
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    terrains = models.CharField(max_length=100)
    climates = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Returns the name of the planet when converted to a string

    class Meta:
        verbose_name = 'Planet'  # Singular name for the model in the admin interface
        verbose_name_plural = 'Planets'  # Plural name for the model in the admin interface
