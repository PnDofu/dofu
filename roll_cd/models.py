from django.db import models

# Create your models here.
class Song(models.Model):
    song_name=models.CharField(max_length=100,unique=True)
    audio_file=models.FileField(upload_to='audio_files/')
    release_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.song_name
    