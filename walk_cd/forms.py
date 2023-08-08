from .models import Songs_0
from django import forms
class Song_form(forms.ModelForm):
    class Meta:
        model=Songs_0
        fields=['song_name','song_file']