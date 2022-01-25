from django.conf import settings
from django.db import models
from django.utils import timezone

class  Musicians(models.Model):
    name=models.CharField(max_length=70)
    SSN=models.IntegerField(default=0)

    def __str__(self):
        return self.name        

class  Band(models.Model):
    group_name=models.CharField(max_length=70)
    foundation_year=models.DateTimeField('date published')
    musicians=models.ForeignKey(Musicians, on_delete=models.CASCADE)
    def __str__(self):
        return self.group_name, self.musicians

class  Album(models.Model):
    album_name=models.CharField(max_length=70)
    release_year=models.DateTimeField('date published')
    band_name=models.ForeignKey(Band, on_delete=models.CASCADE)
    def __str__(self):
        return self.album_name