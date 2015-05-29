from django.db import models

# Create your models here.
class Tracks(models.Model):
	tittle = models.CharField(max_lenght=255)
	order  = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	track_file = models.FileField(upload_to='tracks')
