from rest_framework import serializers
from .models import Placement

class PlacementSerializer(serializers.ModelSerializer):
    # Including student's username for better readability (optional)
    # student_username = serializers.CharField(source='student.username', read_only=True)
    
    class Meta:
        model = Placement
        fields = '__all__'