# !usr/bin/env python3
import os
import random

import youtube_dl
import pygame
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials




#global variables
song_name = " "

artist = " "
guess_count = 0


# Create a list of popular songs
song_list = []


# Import songs from a music database into empty song_list


# randomly shuffle songs and play a 5 second audio clip


# User has 2 chances to enter the correct song name

guess = input("Name this song")

answer = song_name

if guess == answer:
    print("Yes, you are listening to:", song_name, "written by:", artist)

elif guess != answer and guess_count == 1:
    print("Sorry", guess.upper(), "is not correct. Please try again!\n Attempt Remaining: 1")
    guess_count += 1

else guess != answer and guess_count == 2:
    print("OoooF, you almost had it! The song you are looking for is:", song_name, "by", artist)


#method to play an audio file in python


