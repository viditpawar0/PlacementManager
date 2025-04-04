from django.db import models

# Create your models here.

class PredictionInput(models.Model):
    cgpa = models.FloatField()
    internships = models.IntegerField()
    projects = models.IntegerField()
    technical_skills = models.IntegerField()
    aptitude_test_score = models.FloatField()
    soft_skills = models.IntegerField()

    class Meta:
        managed = False  # This ensures Django won't create a table for this model
