from rest_framework import serializers
from .models import PredictionInput

class PredictionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionInput
        fields = ['cgpa', 'internships', 'projects', 'technical_skills', 
                 'aptitude_test_score', 'soft_skills']