import os
import re
import urllib.request
import spotipy
from pytube import YouTube
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "fb678d0c376249afac167ee1e0c46d73"
CLIENT_SECRET = "0c5da770ed1e4d9bad0885cc9eb06ee0"
songList = []
baseDownloadPath = "C:/Users/LAKSHYA KUMAR/PycharmProjects/pythonProject/songDownloads"

playlist_link = input()
a = playlist_link.replace("https://open.spotify.com/playlist/", "")
URI, c = a.split("?")

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

userPlaylistName = str(session.user_playlist(user=None, playlist_id=URI, fields="name")["name"])
tracks = session.playlist_tracks(URI)["items"]

for track in tracks:
    songName = track["track"]["name"]
    artistName = ", ".join([artist["name"] for artist in track["track"]["artists"]])

    songInfo = songName + " - " + artistName
    songList.append(songInfo)


def scrapeYt(query):
    userQuery = query.replace(" ", "+")
    baseLink = "https://www.youtube.com/results?search_query="
    bytesQueryLink = str(bytes(str(baseLink + userQuery), 'utf-8'))
    queryLink = bytesQueryLink[2:][:-1]

    html = urllib.request.urlopen(queryLink)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    final_link = str("https://youtu.be/" + video_ids[0])
    print(final_link)
    return final_link


def downloadVideo(URL, songName):
    downloadFolder = baseDownloadPath + "/" + userPlaylistName
    if not os.path.exists(downloadFolder):
        os.mkdir(downloadFolder)
    name = str(songName) + ".mp3"
    yt = YouTube(URL)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=downloadFolder, filename=name)


for item in songList:
    downloadVideo(scrapeYt(item), item)
    print("Downloaded  " + item)

print("Program Executed Successfully")

z = "https://open.spotify.com/playlist/27kGZlgaYCmsv52b1w7JFW?si=a0a537dff6fc4714"
