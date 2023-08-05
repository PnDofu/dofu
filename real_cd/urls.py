from django.urls import path
from .views import upload_song,song_list,delete_song,play_back
app_name="dofu_cd"
urlpatterns=[
    path("upload_song/",upload_song,name="upload_song"),
    path("song_list/",song_list,name="song_list"),
    path("delete_song/<int:song_id>/",delete_song,name="delete_song"),
    path("play_back/<int:song_id>/",play_back,name="play_back"),
]