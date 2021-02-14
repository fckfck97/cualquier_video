from django.http import HttpResponse
from django.shortcuts import render
import youtube_dl
from .forms import Form_Descarga
import re
def buscar_video(request):
    global context
    form = Form_Descarga(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex1 = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        regex2 = r'^(http(s)?:\/\/)?((es).)?pornhub?(\.com)?\/.+'
        regex3 = r'^(http(s)?:\/\/)?((w){3}.)?instagram?(\.com)?\/.+'
        regex4 = r'^(http(s)?:\/\/)?twitter?(\.com)?\/.+'
        #regex = (r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$\n")
        if re.match(regex1, video_url):
            return(vy(request,video_url,form))
        elif re.match(regex2,video_url):
        	return(vp(request,video_url,form))
        elif re.match(regex3,video_url):
        	return(vi(request,video_url,form))
        elif re.match(regex4,video_url):
        	return(vt(request,video_url,form))
    return render(request, 'videos_mp3/home.html', {'form': form})

def vy(request,video_url,form):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(
			video_url, download=False)
	video_audio_streams = []
	for m in meta['formats']:
		file_size = m['filesize']
		if file_size is not None:
			file_size = f'{round(int(file_size) / 1000000,2)} mb'
		
		resolution = 'Audio'
		if m['height'] is not None:
			resolution = f"{m['height']}x{m['width']}"
			video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
	video_audio_streams = video_audio_streams[::-1]
	context = {
            'form': form,
            'title': meta['title'], 'streams': video_audio_streams,
            'description': meta['description'], 'likes': meta['like_count'],
            'dislikes': meta['dislike_count'], 'thumb': meta['thumbnails'][3]['url'],
            'duration': round(int(meta['duration'])/60, 2), 'views': f'{int(meta["view_count"]):,}'
        }
	return render(request, 'videos_mp3/home2.html', context)
#pornhub
def vp(request,video_url,form):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(video_url, download=False)
	video_audio_streams = []
	for m in meta['formats']:
		if m['height'] is not None:
			resolution = f"{m['height']}x{m['width']}"
			video_audio_streams.append({
	                'resolution': resolution,
	                'extension': m['ext'],
	                'video_url': m['url']})
	video_audio_streams = video_audio_streams[::-1]
	context = {
            'form': form,
            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
            'duration': round(int(meta['duration'])/60, 2), 'views': f'{int(meta["view_count"]):,}'}
	return render(request, 'videos_mp3/home3.html', context)
#instagram
def vi(request,video_url,form):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(video_url, download=False)
	video_audio_streams = []
	for m in meta['formats']:
		if m['height'] is not None:
			resolution = f"{m['height']}x{m['width']}"
			video_audio_streams.append({
	                'resolution': resolution,
	                'extension': m['ext'],
	                'video_url': m['url']})
	video_audio_streams = video_audio_streams[::-1]
	context = {
            'form': form,
            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
            'duration': meta['timestamp'], 'like': meta['like_count'],
            'comentarios': meta['comment_count']}
	return render(request, 'videos_mp3/home4.html', context)



#twitter
def vt(request,video_url,form):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(video_url, download=False)
	video_audio_streams = []
	for m in meta['formats']:
		if m['height'] is not None:
			resolution = f"{m['height']}x{m['width']}"
			video_audio_streams.append({
	                'resolution': resolution,
	                'extension': m['ext'],
	                'video_url': m['url']})
	video_audio_streams = video_audio_streams[::-1]
	context = {
            'form': form,
            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
            'duration': meta['timestamp'], 'like': meta['like_count'],
            'comentarios': meta['comment_count']}
	return render(request, 'videos_mp3/home5.html', context)
