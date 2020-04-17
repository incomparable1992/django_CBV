from django.db import models
from datetime import datetime

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'NOTE'
        managed = True

    def __str__(self):
        return self.title
