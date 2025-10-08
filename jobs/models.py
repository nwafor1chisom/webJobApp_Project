from django.db import models
from django.conf import settings
from django.utils import timezone

class JobPost(models.Model):
    CATEGORY_CHOICES = (
        ('tech', 'Tech'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('finance', 'Finance'),
        ('other', 'Other'),
    )

    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    deadline = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
