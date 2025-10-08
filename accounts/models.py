from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def is_employer(self):
        return self.role == 'employer'

    def is_job_seeker(self):
        return self.role == 'job_seeker'

