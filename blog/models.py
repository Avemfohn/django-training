from django.conf import settings
from django.db import models
from django.utils import timezone

class  Musicians(models.Model):
    name=models.CharField(max_length=70)
    SSN=models.IntegerField(default=0)

    def __str__(self):
        return self.name        