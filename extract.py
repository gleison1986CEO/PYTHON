import os
import openai ## install openai pip install openai==0.25.0
from dotenv import load_dotenv  ## LOAD ENV STRINGS FROM .env
from save     import SAVE
from quiz     import QUIZ


#====================>
Save           =  SAVE()
Quizes         =  QUIZ()
load_dotenv()
#====================>

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  ## OPENAI .ENV FILE
openai.api_key = OPENAI_API_KEY

class EXTRACTS():
    def extractsTextsDownload(self,hash):
        audio_file     = open("audios/" + str(hash) + ".mp3", "rb")   ## GET AND OPEN PATH MP3 AUDIO DONWLOAD
        transcript     = openai.Audio.transcribe("whisper-1", audio_file)  ## EXTRACT TEXT FROM AUDIO WITH GPT
        text           = transcript.text  ## OUT TEXT
        Save.Save(text, hash) ## this text will pass data to another function on save data
        print('generate text') ## FOR TESTE
        print(text) ## FOR TESTE
        print('generate quizes') ## FOR TESTE
        return text
       

       
