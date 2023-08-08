from .models import Song
from django import forms
class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=['song_name','audio_file']
        