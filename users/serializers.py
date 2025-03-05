from rest_framework import serializers
from users.models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        
        fields = ['username', 'email', 'role', 'first_name', 'last_name', 'date_joined', 'course_pursuing', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # Ensure course_pursuing is only set for students
        if data.get('role') == 'admin' and 'course_pursuing' in data:
            data.pop('course_pursuing', None)
        
        # Validate that course_pursuing is within allowed choices
        if data.get('course_pursuing') and data.get('course_pursuing') not in dict(CustomUser.COURSE_CHOICES):
            raise serializers.ValidationError({"course_pursuing": "Invalid course selected."})
        
        return data

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
