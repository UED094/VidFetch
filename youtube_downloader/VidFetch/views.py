from django.shortcuts import render
from pytube import YouTube

from .forms import DownloadForm


def download_video(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['url']
            try:
                # Create a YouTube object with the video URL
                video = YouTube(video_url)
                # Get the highest resolution available
                stream = video.streams.get_highest_resolution()
                # Start the download
                stream.download()
                message = "Download complete!"
            except Exception as e:
                message = "Error: " + str(e)
    else:
        form = DownloadForm()
        message = ""

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'VidFetch/download.html', context)
