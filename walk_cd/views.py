from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import Songs_0
from .forms import Song_form
# Create your views here.

def play_back(request):
    song_list=Songs_0.objects.all()
    return render(request,'walk_cd/play_back.html',{'song_list':song_list})
def upload_song(request):
    if request.method == 'POST':
        form = Song_form(request.POST, request.FILES)
        if form.is_valid():
            song_name = form.cleaned_data['song_name']
            song_file = form.cleaned_data['song_file']
            existing_song = Songs_0.objects.filter(song_name=song_name).first()
            if existing_song:
                pass
            else:
                form.save()
                return redirect('dofu_0:play_back')
        else:
            # 表单验证失败，传递错误信息给模板
            return render(request, 'walk_cd/upload_song.html', {'form': form})
    else:
        form = Song_form()
    return render(request, 'walk_cd/upload_song.html', {'form': form})
def song_list(request):
    cd_list=Songs_0.objects.all()
    return render(request,'walk_cd/song_list.html',{'cd_list':cd_list})

def delete_song(request,song_id):
    if request.method=='POST':
        song=get_object_or_404(Song_0,id=song_id)
        song.delete()
        return redirect('dofu_0:song_list')