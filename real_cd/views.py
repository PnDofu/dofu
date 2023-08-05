from django.shortcuts import render,redirect,get_object_or_404
from .models import Song,Lyric
from django.template.defaultfilters import escape
from django.db.models import Max
# Create your views here.
def upload_song(request):
    if request.method=="POST":
        name=request.POST["name"]
        audio_file=request.FILES["audio_file"]
        lyr_file=request.FILES["lyr_file"]
        song=Song.objects.create(name=name,audio_file=audio_file)
        lyrics=lyr_file.read().decode('utf-8')
        lyric_lines=lyrics.splitlines()
        for line in lyric_lines:
            Lyric.objects.create(song=song,text=line)
        return redirect("dofu_cd:song_list")
    return render(request,"real_cd/upload_song.html")
def song_list(request):
    songs=Song.objects.all()
    return render(request,"real_cd/song_list.html",{"songs":songs})
def delete_song(request,song_id):
    song=get_object_or_404(Song,pk=song_id)
    if request.method=="POST":
        song.delete()
        return redirect("dofu_cd:song_list")
    return render(request,"real_cd/delete_song.html",{"song":song})
def play_back(request,song_id):
    max_song_id = Song.objects.all().order_by('-id').first().id
    song=Song.objects.get(pk=song_id)
    lyrics=Lyric.objects.filter(song=song)
    lyric_text='\n'.join(f"{escape(lyric.text)}" for lyric in lyrics)
    return render(request,"real_cd/play_back.html",{"song":song,"lyrics":lyric_text,"max_id":max_song_id})


