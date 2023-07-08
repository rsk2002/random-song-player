'''
    Author : Rahul S Kumar
    Github : https://github.com/rsk2002
    Usage  : This program is used to play randomly selected songs from a folder and play it at 50% volume, using the VLC mediaplayer. This program uses vlc library which could be 
             installed using the command 'pip install python-vlc'.
'''

#Import necessary libraries
import os
import random
import time
import vlc

#Set path to the music files
path = '/home/rahul/Music/chill_station'
l = os.listdir(path)

#Set number of tracks to be played
no_of_tracks = 2

#Select the index of random songs
rand_songs = random.sample(range(len(l)), no_of_tracks)

#Initialise VLC media player
media_player = vlc.MediaListPlayer()
player = vlc.Instance()
media_list = vlc.MediaList()

#Add the selected songs to the playlist
for i in rand_songs:
    p = path + '/' + l[i]
    print(p)
    media = player.media_new(p)
    media_list.add_media(media)

media_player.set_media_list(media_list)

#Set the volume percentage and play the music
media_player.get_media_player().audio_set_volume(50)
media_player.play()

while media_player.is_playing():
    time.sleep(10)

#Set the volume back to 150 and shutdown
media_player.get_media_player().audio_set_volume(150)
print("Playlist completed...!")