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
        regex5 = r'^(http(s)?:\/\/)?((w){3}.)?facebook?(\.com)?\/.+'
        #regex = (r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$\n")
        if re.match(regex1, video_url):
            return(vy(request,video_url,form))
        elif re.match(regex2,video_url):
        	return(vp(request,video_url,form))
        elif re.match(regex3,video_url):
        	return(vi(request,video_url,form))
        elif re.match(regex4,video_url):
        	return(vt(request,video_url,form))
        elif re.match(regex5,video_url):
        	return(vf(request,video_url,form))  
    return render(request, 'videos_mp3/home.html', {'form': form})

def vy(request,video_url,form):
	try:
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
				if resolution == "144x256" or resolution == "144x192":
					resolution = "144p"
				if resolution == "240x426" or resolution == "240x320":
					resolution = "240p"
				if resolution == "360x640" or resolution == "360x480":
					resolution = "360p"
				if resolution == "480x640" or resolution == "480x854":
					resolution = "480p"
				if resolution == "720x1280":
					resolution = "720p HD"
				if resolution == "1080x1920":
					resolution = "1080p HD"
				if resolution == "1440x2560":
					resolution = "1440p 2K"
				if resolution == "2160x3840":
					resolution = "2160p 4K"
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
	except:
		context = {'form':form}
		return render(request,'videos_mp3/error.html', context)
#pornhub
def vp(request,video_url,form):
	try:
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
	except:
		context = {'form':form}
		return render(request,'videos_mp3/error.html', context)
#instagram
def vi(request,video_url,form):
	try:
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
		if meta['comment_count'] == None:
			meta['comment_count'] = "No hay comentarios en este Video"
		context = {
	            'form': form,
	            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
	            'like': meta['like_count'],'comentarios': meta['comment_count'], 'descripcion': meta['description'],
	            'subido':meta['uploader']}
		return render(request, 'videos_mp3/home4.html', context)
	except:
		context = {'form':form}
		return render(request,'videos_mp3/error.html', context)



#twitter
def vt(request,video_url,form):
	try:
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
		if meta['comment_count'] == None:
			meta['comment_count'] = "No hay comentarios en este Video"
		context = {
	            'form': form,
	            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
	            'duration': round(int(meta['duration'])/60, 2), 'like': meta['like_count'],
	            'comentarios': meta['comment_count'], 'descripcion': meta['description'],
	            'subido':meta['uploader']}
		return render(request, 'videos_mp3/home5.html', context)
	except:
		context = {'form':form}
		return render(request,'videos_mp3/error.html', context)

#facebook
def vf(request,video_url,form):
	try:
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
		if meta['comment_count'] == None:
			meta['comment_count'] = "No hay comentarios en este Video"
		context = {
	            'form': form,
	            'title': meta['title'], 'streams': video_audio_streams,'thumb': meta['thumbnail'],
	            'duration': meta['timestamp'], 'like': meta['like_count'],
	            'comentarios': meta['comment_count']}
		return render(request, 'videos_mp3/home6.html', context)
	except:
		context = {'form':form}
		return render(request,'videos_mp3/error.html', context)