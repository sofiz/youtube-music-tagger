import os
from mp3_tagger import MP3File
basepath = (r'C:\Users\sofiz\Desktop\folders\test')
for entry in os.listdir(basepath):
 if entry.endswith(".mp3"):
   print (entry)
   entry_artist = entry.partition("-")[0]
   print ("artist 1 : ", entry_artist)
   entry_title = entry.partition("-")[2]
   print(entry_title)
   if "ft" in entry_title :
       artist = entry_title.partition("ft. ")[2]
       print ("artist 2 : " , artist)
       entry_title = entry_title.partition("ft. ")[0]
   entry_title = entry_title.partition("(" or "[" or "." or "ft")[0]
   print("song name : ", entry_title)
   entry_name = entry_title
   p= (basepath + "/")
   if (entry_name!=""):
       audiofile = MP3File( p + entry)
       audiofile.artist = (entry_artist + " / " + artist)
       audiofile.song = (entry_title)
       audiofile.save()
       os.rename ( p + entry , p + entry_name + ".mp3")
