from django.db import models


class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.FileField(
        upload_to="files/",
    )
    created_at = models.DateTimeField(auto_now_add=True)
