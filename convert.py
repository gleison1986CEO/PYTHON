
import os
import time
import moviepy.editor as mp  ## VIDEO TO MP3  CONVERTER  MODULE MOVIEPY



class CONVERTVIDEOS():
    def ConvertVideos(self, hash):

        try:

            time.sleep(2)
            #======================CONVERTER
            clip = mp.VideoFileClip('videos/' + str(hash) + '.mp4')         ## GET MP4 PATH OPEN 
            clip.audio.write_audiofile('audios/' + str(hash) + '.mp3')      ## GET MP4 PATH OPEN AND CONVERTER TO MP3
            #======================CONVERTER
            time.sleep(2)

        except:
            print("ERROR!")
        print("Your Videos is Converte to MP3 Now!")






