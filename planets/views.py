from .models import Planet
from .serializers import PlanetSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import generics
from rest_framework.response import Response

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

class RegisterView(generics.CreateAPIView):
    """
    A view for registering new users.

    This view inherits from CreateAPIView, providing a default implementation for
    handling POST requests to create new users.

    Attributes:
        queryset (QuerySet): All instances of the User model.
        serializer_class (Serializer): Serializer class used to transform User instances into JSON.
    """

    queryset = User.objects.all()  # Query all User objects from the database
    serializer_class = RegisterSerializer  # Serializer class for serializing User objects

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to register new users.

        This method validates the incoming data using the serializer and creates a new
        user if the data is valid. It returns a success message upon successful registration
        or error messages if the data is invalid.

        Args:
            request (Request): The HTTP request object containing the data to be validated.

        Returns:
            Response: A response object containing the success message or error messages.
        """
        serializer = self.get_serializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():  # Check if the data is valid
            user = serializer.save()  # Save the new user instance
            return Response({
                "message": f"User {user.username} successfully registered."  # Success message
            }, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  # Return validation errors
