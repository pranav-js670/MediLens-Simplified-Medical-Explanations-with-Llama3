from django.db import models

# Create your models here.
class Transcripts(models.Model):
    text = models.TextField(max_length=20)

    def __str__(self):
        return self.text
