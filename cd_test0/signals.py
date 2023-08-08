from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Cd_test
import os
@receiver(pre_delete,sender=Cd_test)
def delete_cd_file(sender,instance,**kwargs):
    if instance.cd_file:
        if os.path.isfile(instance.cd_file.path):
            os.remove(instance.cd_file.path)