from .models import Song
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
@receiver(pre_delete,sender=Song)
def delete_audio_file(sender,instance,**kwargs):
    if instance.audio_file:
        if os.path.isfile(instance.audio_file.path):
            os.remove(instance.audio_file.path)