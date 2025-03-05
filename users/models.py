from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )

    COURSE_CHOICES = (
        ('computer_science', 'Computer Science'),
        ('data_science', 'Data Science'),
        ('business_management', 'Business Management'),
        ('mechanical_engineering', 'Mechanical Engineering'),
        ('electrical_engineering', 'Electrical Engineering'),
        ('civil_engineering', 'Civil Engineering'),
        ('biotechnology', 'Biotechnology'),
        ('economics', 'Economics'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    course_pursuing = models.CharField(
        max_length=50, 
        choices=COURSE_CHOICES, 
        blank=True, 
        null=True, 
        help_text="Course the student is pursuing"
    )

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.course_pursuing = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
