from django.db import models

# Create your models here.
class Songs_0(models.Model):
    song_name=models.CharField(max_length=100,unique=True)
    song_file=models.FileField(upload_to='song_files/')
    