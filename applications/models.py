from django.db import models
from django.conf import settings
from jobs.models import JobPost
from django.utils import timezone

def resume_upload_path(instance, filename):
    return f'resumes/{instance.user.username}/{filename}'

class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to=resume_upload_path)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'job')  # Prevent duplicate applications

    def __str__(self):
        return f'{self.user.username} -> {self.job.title}'
