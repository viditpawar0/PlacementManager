from rest_framework import serializers
from users.models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password in API response
        }

    def create(self, validated_data):
        # Create user with hashed password
        user = CustomUser.objects.create_user(**validated_data)
        return user
