from .views import all_songs,upload_song
from django.urls import path
app_name='dofu'
urlpatterns=[
    path('all_song/',all_songs,name='all_song'),
    path('upload_song',upload_song,name='upload_song'),
]