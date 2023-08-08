from django import forms
from .models import Cd_test
class SongForm(forms.ModelForm):
    class Meta:
        model=Cd_test
        fields=['name','cd_file']