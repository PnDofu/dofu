from django.db import models
import os
from django.dispatch import receiver
# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=100,unique=True)
    audio_file=models.FileField(upload_to="dofu_file/")
@receiver(models.signals.pre_delete,sender=Song)
def delete_audio_file(sender,instance,**kwargs):
    if instance.audio_file:
        if os.path.isfile(instance.audio_file.path):
            os.remove(instance.audio_file.path)
class Lyric(models.Model):
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    text=models.TextField()
    lyr_file=models.FileField(upload_to="cd_lyr/")

    
