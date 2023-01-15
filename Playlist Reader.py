import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "fb678d0c376249afac167ee1e0c46d73"
CLIENT_SECRET = "0c5da770ed1e4d9bad0885cc9eb06ee0"
songList = []

playlist_link = input()
a = playlist_link.replace("https://open.spotify.com/playlist/", "")
URI, c = a.split("?")

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

userPlaylistName = session.user_playlist(user=None, playlist_id=URI, fields="name")
tracks = session.playlist_tracks(URI)["items"]

for track in tracks:
    songName = track["track"]["name"]
    artistName = ", ".join([artist["name"] for artist in track["track"]["artists"]])

    songInfo = songName + " - " + artistName
    songList.append(songInfo)

print(songList)

print("Program Executed Successfully")
