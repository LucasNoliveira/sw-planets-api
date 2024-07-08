from rest_framework import serializers
from .models import Planet
from django.contrib.auth.models import User

class PlanetSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Planet model.

    This serializer inherits from ModelSerializer, providing a convenient way
    to serialize and deserialize Planet model instances to and from JSON.

    Attributes:
        model (Model): Specifies the model class to be serialized.
        fields (str or tuple): Controls which fields are included in the serialized output.
                                '__all__' includes all fields from the Planet model.

    Note:
        This serializer assumes that the Planet model is defined and imported from .models.
    """

    class Meta:
        model = Planet  # Specifies the model class to be serialized
        fields = '__all__'  # Includes all fields from the Planet model in the serialized output
        

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user