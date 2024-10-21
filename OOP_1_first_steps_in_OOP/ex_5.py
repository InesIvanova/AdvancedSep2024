class Music:
    def __init__(self, title: str, artist: str, lyrics: str, *args):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.co_authors = args

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("hello", 5, "Hello, I am here, nice to see you, hello")
print(song.print_info())
print(song.play())
