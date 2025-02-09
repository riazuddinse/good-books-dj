from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, blank=False, default=uuid.uuid4)
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return super().__str__(self.title)