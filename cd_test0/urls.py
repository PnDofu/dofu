from django.urls import path
from . import views
app_name='dofu_1'
urlpatterns=[
    path('song_list/',views.song_list,name='song_list'),
    path('upload_song/',views.upload_song,name='upload_song'),
    path('delete_song/<int:cd__test_id>/',views.delete_song,name='delete_song'),
    path('play/',views.play_back,name='play'),
]