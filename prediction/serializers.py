from rest_framework import serializers
from .models import PredictionInput

class PredictionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionInput
        fields = ['cgpa', 'internships', 'projects', 'workshops_certifications',
                 'aptitude_test_score', 'soft_skills', 'extracurricular_activities', 'placement_training']