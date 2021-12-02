from django.shortcuts import render
from googleapiclient.discovery import build
import pafy
from django.http import request
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

# keyword = "Bahati and Diana"
def result(request): 
    api_key="AIzaSyC38udAOc03YcEXO41SwnqxPJEjpaxudio"
    
    if request.GET:
        keyword = request.GET.get('search_item')
        print(keyword+ 'is the inputted text')
        context = {}
        youtube = build('youtube','v3',developerKey = api_key)
        print(type(youtube))

        request = youtube.search().list(q=keyword,part='snippet',type='video')
        print(type(request))
        res = request.execute()
        
        for item in res['items']:
            # print(res['items'])
            print(type(res['items']))
            videoId=item['id']['videoId']
            print(type(videoId))
            videoUrl = "https://www.youtube.com/watch?v="+videoId 
            print(videoUrl)
            
            # url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
            video = pafy.new(videoUrl)
            file_size = video.duration

            '''Get the best audio file for download'''
            bestaudiodownload = video.getbestaudio()
            print(type(video))

            details = {video.title:{"videoTitle":video.title,"fileSize":file_size,"videoUrl":videoUrl,"videoAuthor":video.author,"likes":video.likes,"duration":video.duration,"bestQuality":bestaudiodownload}}
            context.update(details)
            print(context)

        # return video.title,videoUrl,video.author,video.duration,video.viewcount,video.likes,bestaudiodownload
    print(context)
    # return render(request,'index.html')
    return HttpResponse(context)

def download(request):
    videoId = request.GET.get('videoId')
    download_item = pafy.new(videoId)
    s = download_item.getbest()
    filename = s.download()
            