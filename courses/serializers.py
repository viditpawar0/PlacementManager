from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'student_username', 'name', 'description', 'duration', 'certification', 'created_at']
