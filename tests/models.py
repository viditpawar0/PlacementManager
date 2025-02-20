from django.db import models
from users.models import CustomUser

class Test(models.Model):
    TEST_TYPE = (
        ('core', 'Core'),
        ('aptitude', 'Aptitude'),
    )
    
    name = models.CharField(max_length=255)
    course = models.TextField()
    description = models.TextField()
    syllabus = models.TextField()
    test_type = models.CharField(max_length=10, choices=TEST_TYPE)
    duration = models.IntegerField(help_text="Duration in minutes")
    total_marks = models.IntegerField()
    date = models.DateField() 

    def __str__(self):
        return self.name

class TestResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    rank = models.IntegerField(blank=True, null=True) 
    percentage = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True) 

    def save(self, *args, **kwargs):
        # Auto-calculate percentage and status
        self.percentage = (self.score / self.test.total_marks) * 100
        self.status = "Pass" if self.percentage >= 40 else "Fail" 

        # Auto-generate rank
        existing_results = TestResult.objects.filter(test=self.test).order_by('-score')
        rank = 1
        for result in existing_results:
            if result.score > self.score:
                rank += 1
        self.rank = rank
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.username} - {self.test.name} (Rank: {self.rank})"
