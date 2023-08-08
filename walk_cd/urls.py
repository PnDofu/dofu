from .views import play_back,upload_song,song_list,delete_song
from django.urls import path
app_name='dofu_0'
urlpatterns=[
    path('play_back/',play_back,name='play_back'),
    path('upload_song/',upload_song,name='upload_song'),
    path('song_list/',song_list,name='song_list'),
    path('delete_song/<int:song_id>/',delete_song,name='delete_song'),
]