from rest_framework import serializers
from .models import Placement
from users.models import CustomUser

class PlacementSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(
        queryset=CustomUser.objects.filter(role='student'), slug_field='username'
    )
    class Meta:
        model = Placement
        fields = '__all__'