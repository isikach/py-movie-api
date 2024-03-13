from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movie"

    def __str__(self):
        return f"Movie: {self.title} (duration: {self.duration})"
