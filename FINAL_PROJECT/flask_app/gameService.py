import os
import random
from googleapiclient.discovery import build  # Import Google API client for YouTube
from spotipy.oauth2 import SpotifyClientCredentials  # Import Spotify credentials manager
import spotipy  # Import Spotify API library
from FINAL_PROJECT.song import Song  # Import the Song model
from FINAL_PROJECT.state import state  # Import the GameState model
import yt_dlp as youtube_dl

import re

class GameService:
    """
    The GameService class handles the core logic of the game, 
    including fetching songs from YouTube and Spotify, managing rounds, and updating the game state.
    """

    def __init__(self):
        """
        Initialize the game service by setting up the game state and API clients for YouTube and Spotify.
        """
        print("Initializing GameService...")

        self.game_state = state()  # Create a new game state instance
        print(f"Initialized GameState: {self.game_state}")

        # Load API keys from environment variables
        self.youtube_api_key = os.getenv('YOUTUBE_API_KEY')
        self.spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        print("Loaded API keys from environment variables:")
        # print(f"  YouTube API Key: {self.youtube_api_key}")
        # print(f"  Spotify Client ID: {self.spotify_client_id}")
        # print(f"  Spotify Client Secret: {self.spotify_client_secret}")

        # Initialize the Spotify API client
        try:
            self.spotify = spotipy.Spotify(
                client_credentials_manager=SpotifyClientCredentials(
                    client_id=self.spotify_client_id,
                    client_secret=self.spotify_client_secret
                )
            )
            print("Spotify API client initialized successfully.")
        except Exception as e:
            print("Error initializing Spotify API client:", e)

    def fetch_youtube_playlist(self, playlist_id):
        """
        Fetch a playlist from YouTube using the playlist ID and extract song information.

        Parameters:
        - playlist_id (str): The ID of the YouTube playlist to fetch.

        Returns:
        - dict: A dictionary with song titles as keys and Song objects as values.
        """
        print(f"Fetching YouTube playlist with ID: {playlist_id}")
        try:
            youtube = build('youtube', 'v3', developerKey=self.youtube_api_key)  # Build the YouTube API client
            print("YouTube API client initialized.")
            
            request = youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=30  # Fetch a maximum of 30 songs from the playlist
            )
            response = request.execute()  # Execute the API request
            print("YouTube API request executed successfully.")
            
            playlist = {}

            # Loop through each item in the playlist response and extract song data
            for item in response['items']:
                title = item['snippet']['title']
                artist = item['snippet']['videoOwnerChannelTitle']
                url = item['snippet']['resourceId']['videoId']
                print(f"Found song: Title='{title}', Artist='{artist}', URL='{url}'")

                # Create a Song object and add it to the playlist dictionary
                playlist[title] = Song(
                    title=title,
                    artist=artist,
                    album='',
                    album_cover=f'https://www.youtube.com/watch?v={url}'  # Construct the YouTube video URL
                )
            print(f"Fetched {len(playlist)} songs from the playlist.")
            return playlist

        except Exception as e:
            print("Error fetching YouTube playlist:", e)
            return {}

    def get_spotify_song(self, title, artist):
        """
        Search for a song on Spotify by title and artist, and return song details.

        Parameters:
        - title (str): The title of the song.
        - artist (str): The name of the artist.

        Returns:
        - Song: A Song object with details from Spotify, or None if no match is found.
        """
        print(f"Searching for song on Spotify: Title='{title}', Artist='{artist}'")
        query = f'{artist} {title}'  # Construct the search query
        print(f"Spotify search query: '{query}'")
        
        try:
            result = self.spotify.search(q=query, type='track', limit=1)  # Search Spotify for the song
            print("Spotify API search executed successfully.")

            # Check if any tracks were found
            if result['tracks']['items']:
                track = result['tracks']['items'][0]  # Get the first track in the search results
                print(f"Found song on Spotify: Name='{track['name']}', Artist='{track['artists'][0]['name']}', Album='{track['album']['name']}'")
                
                # Create and return a Song object with details from Spotify
                return Song(
                    title=track['name'],
                    artist=track['artists'][0]['name'],
                    album=track['album']['name'],
                    album_cover=track['album']['images'][0]['url']
                )
            else:
                print("No matching song found on Spotify.")
                return None  # Return None if no matching song is found

        except Exception as e:
            print("Error searching for song on Spotify:", e)
            return None

    def increment_round(self):
        """
        Increment the current game round by calling the GameState method.
        """
        print(f"Incrementing round. Current round: {self.game_state.current_round}")
        self.game_state.increment_round()
        print(f"New round: {self.game_state.current_round}")

    def update_score(self, points):
        """
        Update the player's score by the specified number of points.

        Parameters:
        - points (int): The number of points to add to the score.
        """
        print(f"Updating score. Current score: {self.game_state.score}. Points to add: {points}")
        self.game_state.update_score(points)
        print(f"New score: {self.game_state.score}")

    def is_game_over(self):
        """
        Check if the game is over (i.e., if the maximum number of rounds has been reached).

        Returns:
        - bool: True if the game is over, False otherwise.
        """
        game_over = self.game_state.is_game_over()
        print(f"Checking if game is over. Result: {game_over}")
        return game_over

    def download_audio_clip(self, song_url, audio_path):
        """
        Download an audio clip from a YouTube video using the provided URL and save it as a WAV file.

        Parameters:
        - song_url (str): The URL of the YouTube video to download.
        - audio_path (str): The directory path where the audio file will be saved.

        Returns:
        - bool: True if the download and conversion were successful, False otherwise.
        """
        if song_url is None:
            print("No URL returned")
            return None

        ytdl_opts = {
            'quiet': True,
            'format': 'bestaudio/best',
            'outtmpl': f'{audio_path}/%(title)s.%(ext)s',  # Adjusted the outtmpl path
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',  # Use wav format for compatibility
                'preferredquality': '192',
            }],
            'verbose': True,
        }

        print(f"Downloading audio clip from URL: {song_url}")
        try:
            with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
                ytdl.download([song_url])
                print(f"Downloaded and converted to WAV: {audio_path}")
                return True
        except Exception as e:
            print(f"Error downloading video: {e}")
            return False

    def sanitize_filename(self, filename):
        """
        Sanitize a filename by removing invalid characters and replacing spaces with underscores.

        Parameters:
        - filename (str): The filename to sanitize.

        Returns:
        - str: The sanitized filename.
        """
        print(f"Sanitizing filename: {filename}")
        # Remove any characters that aren't alphanumeric, dashes, underscores, or spaces
        filename = re.sub(r'[^\w\s-]', '', filename)
        # Replace spaces with underscores
        filename = filename.replace(' ', '_')
        sanitized = filename.strip()
        print(f"Sanitized filename: {sanitized}")
        return sanitized
