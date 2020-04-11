import os
import re
from mp3_tagger import MP3File

basepath = input('music folder path :')
rename = input("do you want to rename the songs? Y/N ")
blacklist = ["-", ".","[" , "]" , "(", ")" , "_" , "YouTube" , "Video" , "Official", "mp3" , "Audio" , "Lyric" , "Clip"]

for entry in os.listdir(basepath):
 if entry.endswith(".mp3"):
   print(entry)
   entry_artist = entry.partition("-")[0]
   entry_artist =  re.sub(r'|'.join(map(re.escape, blacklist)), '', entry_artist)
   print ("artist 1 : ", entry_artist)
   entry_title = entry.partition("-")[2]
   artist = ""
   if "ft. " in entry_title :
       artist = entry_title.partition("ft. ")[2]
       artist =  re.sub(r'|'.join(map(re.escape, blacklist)), '', artist)
       print ("artist 2 : " , artist)
       entry_title = entry_title.partition("ft. ")[0]
   entry_title = entry_title.partition("(" or "[" or "." )[0]
   entry_title =  re.sub(r'|'.join(map(re.escape, blacklist)), '', entry_title)
   print("song name : ", entry_title)
   entry_name = entry_title
   p= (basepath + "/")
   if (entry_name!=""):
       audiofile = MP3File( p + entry)
       audiofile.artist = (entry_artist + " / " + artist)
       audiofile.song = (entry_title)
       audiofile.save()
       try :
        if (rename=="Y") or (rename=="y"):
           os.rename ( p + entry , p + entry_name + ".mp3")
       except :
           continue
