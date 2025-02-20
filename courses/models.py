from django.db import models
from users.models import CustomUser

class Course(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    certification = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.name}"
