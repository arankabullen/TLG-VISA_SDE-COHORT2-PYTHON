class Song:
    """
    The Song class represents a song with details such as the title, artist, album, 
    and album cover image. This class is used to store and pass song data throughout the application.
    """

    def __init__(self, title, artist, album, album_cover):
        """
        Initialize the song with the given details.

        Parameters:
        - title (str): The title of the song.
        - artist (str): The name of the artist who performed the song.
        - album (str): The name of the album in which the song was released.
        - album_cover (str): The URL to the album cover image.
        """
        self.title = title
        self.artist = artist
        self.album = album
        self.album_cover = album_cover
        
    def to_dict(self):
        """
        Convert the Song object to a dictionary.
        """
        return {
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'album_cover': self.album_cover
        }

    @classmethod
    def from_dict(cls, data):
        """
        Reconstruct a Song object from a dictionary.
        """
        return cls(
            title=data['title'],
            artist=data['artist'],
            album=data['album'],
            album_cover=data['album_cover']
        )