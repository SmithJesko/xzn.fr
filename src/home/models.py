from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    slug = models.CharField(max_length=8)
    original = models.CharField(max_length=256)

    def __str__(self):
        return self.slug
