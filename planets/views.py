from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Importe o IsAuthenticated

from .models import Planet
from .serializers import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [IsAuthenticated]
    
