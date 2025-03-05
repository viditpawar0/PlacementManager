from rest_framework import serializers
from .models import Internship
from users.models import CustomUser

class InternshipSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username', read_only=True)  # Read-only username
    student = serializers.CharField(write_only=True)  # Allow writing username instead of ID

    class Meta:
        model = Internship
        fields = [
            'id', 'student', 'student_username', 'company_name', 'role', 
            'start_date', 'end_date', 'stipend', 'description', 
            'certificate_provided', 'created_at'
        ]

    def create(self, validated_data):
        """Fetch student using username before creating an Internship."""
        username = validated_data.pop('student')  # Get username from request
        try:
            student = CustomUser.objects.get(username=username, role='student')  # Ensure user exists
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'student': 'Student with this username does not exist.'})
        
        validated_data['student'] = student  # Assign student object
        return super().create(validated_data)
