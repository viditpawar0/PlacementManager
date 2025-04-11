from django.db import models

# Create your models here.

class PredictionInput(models.Model):
    cgpa = models.FloatField()
    internships = models.IntegerField()
    projects = models.IntegerField()
    workshops_certifications = models.IntegerField()
    aptitude_test_score = models.FloatField()
    soft_skills = models.IntegerField()
    extracurricular_activities = models.IntegerField()
    placement_training = models.IntegerField()

    class Meta:
        managed = False  # This ensures Django won't create a table for this model
