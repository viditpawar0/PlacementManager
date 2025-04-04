from rest_framework import serializers
from .models import Course
from users.models import CustomUser

class CourseSerializer(serializers.ModelSerializer):
    student = serializers.CharField(write_only=True)  # Accept username as input
    student_username = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'student', 'student_username', 'name', 'description', 'duration', 'certification', 'created_at']

    def create(self, validated_data):
        student_username = validated_data.pop('student')
        try:
            student = CustomUser.objects.get(username=student_username, role='student')
            return Course.objects.create(student=student, **validated_data)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'student': 'Student not found'})
