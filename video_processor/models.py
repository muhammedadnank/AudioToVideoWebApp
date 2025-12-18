from django.db import models

class VideoFile(models.Model):
    original_video = models.FileField(upload_to='videos/original/')
    processed_video = models.FileField(upload_to='videos/processed/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id} uploaded at {self.uploaded_at}"
