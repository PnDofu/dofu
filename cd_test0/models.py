from django.db import models
import os
from django.dispatch import receiver
# Create your models here.
class Cd_test(models.Model):
    name=models.CharField(max_length=100)
    cd_file=models.FileField(upload_to='cd_file')
@receiver(models.signals.pre_delete,sender=Cd_test)
def delete_cd_file(sender,instance,**kwargs):
    if instance.cd_file:
        if os.path.isfile(instance.cd_file.path):
            os.remove(instance.cd_file.path)