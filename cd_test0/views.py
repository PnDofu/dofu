from django.shortcuts import render,redirect,get_object_or_404
from .models import Cd_test
from .forms import SongForm
# Create your views here.
def song_list(request):
    songs=Cd_test.objects.all()
    return render(request,'cd_test0/song_list.html',{'songs':songs})
def upload_song(request):
    if request.method=='POST':
        form=SongForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dofu_1:song_list')
    else:
        form=SongForm()
    return render(request,'cd_test0/upload_song.html',{'form':form})
def delete_song(request,cd__test_id):
    song=get_object_or_404(Cd_test,pk=cd__test_id)
    if request.method=='POST':
        song.delete()
        return redirect('dofu_1:song_list')
    return render(request,'cd_test0/delete_song.html',{'song':song})
def play_back(request):
    song_list=Cd_test.objects.all()
    return render(request,'cd_test0/play.html',{'song_list':song_list})