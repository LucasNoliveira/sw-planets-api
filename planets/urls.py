from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet, RegisterView

# Create a DefaultRouter instance
router = DefaultRouter()

# Register PlanetViewSet with the router for the 'planets' endpoint
router.register(r'planets', PlanetViewSet)

# Define urlpatterns for routing requests
urlpatterns = [
    # Include URLs generated by the router for 'planets' endpoint
    path('', include(router.urls)),
    # Add the register endpoint
    path('register/', RegisterView.as_view(), name='register'),
]
