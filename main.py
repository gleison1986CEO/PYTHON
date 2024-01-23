import os    ### import OS
import time  ### time for sleep any action


from donwload import DONWLOADS
from extract  import EXTRACTS
from convert  import CONVERTVIDEOS
from hashcode import HASH


#=======================>
Hashcode       =  HASH()
Videos         =  DONWLOADS()
Extract        =  EXTRACTS()
Convert        =  CONVERTVIDEOS()
#=======================>


hashcodeRamdon = Hashcode.hashcode() ##HASHCODE GENERATE RAMDON

Videos.Download("https://www.youtube.com/watch?v=oqGZLxPCWlo", str(hashcodeRamdon) )
time.sleep(4)
Convert.ConvertVideos(str(hashcodeRamdon))
time.sleep(4)
Extract.extractsTextsDownload(str(hashcodeRamdon))
time.sleep(1)

 