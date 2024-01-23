
import os
import time
from pytube import YouTube    ## USING PYUBE FOR DOWNLOAD VIDEO

## CLASS DONWLOADS

class DONWLOADS():
    def Download(self, link, hash):  ## LINK DOWNLOADS 

        video = YouTube(link)
        video = video.streams.get_highest_resolution()   ## 720 OU 1080P
        
        try:
            video.download(filename='videos/' + str(hash) + '.mp4')         ## MP4 PATH LOCAL

        except:
            print("ERROR!")
        print("Your video donwload now!")






