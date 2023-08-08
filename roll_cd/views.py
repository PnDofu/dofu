from django.shortcuts import render,redirect
from .models import Song
from .forms import SongForm

# Create your views here.
songs=Song.objects.all().order_by('song_name')
ground_songs={}
for song in songs:
    ground_songs.setdefault(song.song_name,[]).append(song)
for song_name,songs_with_same_name in ground_songs.items():
    if len(songs_with_same_name)>1:
        for song in songs_with_same_name[1:]:
            song.delete()

def all_songs(request):
    songs=Song.objects.all()
    unique_song_names=set()
    unique_songs=[]
    for song in songs:
        if song.song_name not in unique_song_names:
            unique_song_names.add(song.song_name)
            unique_songs.append(song)
    return render(request,'roll_cd/all_songs.html',{'songs':unique_songs})
def upload_song(request):
    if request.method=='POST':
        form=SongForm(request.POST,request.FILES)
        if form.is_valid():
            song_name=form.cleaned_data['song_name']
            audio_file=form.cleaned_data['audio_file']
            existing_song=Song.objects.filter(song_name=song_name).first()
            if existing_song:
                pass
            else:
                form.save
                return redirect('dofu:all_song')
    else:
        form=SongForm()
    return render(request,'roll_cd/upload_song.html',{'form':form})