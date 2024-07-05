from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Planet
from .serializers import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on the Planet model.

    This viewset inherits from ModelViewSet, providing default implementations for
    create, retrieve, update, partial_update, and destroy actions.

    Attributes:
        queryset (QuerySet): All instances of the Planet model.
        serializer_class (Serializer): Serializer class used to transform Planet instances into JSON.
        permission_classes (list): List of permission classes applied to this viewset.
                                    Requires user authentication for access.
    """

    queryset = Planet.objects.all()  # Query all Planet objects from the database
    serializer_class = PlanetSerializer  # Serializer class for serializing Planet objects

    # Apply the IsAuthenticated permission to restrict access to authenticated users only
    permission_classes = [IsAuthenticated]
