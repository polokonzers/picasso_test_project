from django.db import models


class File(models.Model):
    """Describes uploaded files model"""
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
