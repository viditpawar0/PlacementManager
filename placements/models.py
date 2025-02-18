from django.db import models
from users.models import CustomUser

class Placement(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    company = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    date_placed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.company}"
