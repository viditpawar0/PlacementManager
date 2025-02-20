from rest_framework import serializers
from .models import Internship

class InternshipSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Internship
        fields = [
            'id', 'student', 'student_username', 'company_name', 'role', 
            'start_date', 'end_date', 'stipend', 'description', 
            'certificate_provided', 'created_at'
        ]
