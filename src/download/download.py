import pafy

class Download:
    def getDetails():
        url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
        video = pafy.new(url)
        file_size = video.get_filesize()

        '''Get the best audio file for download'''
        bestaudiodownload = video.getbestaudio()

        title,url,author,duration,views,likes = video.title,url,video.author,video.duration,video.viewcount,video.likes