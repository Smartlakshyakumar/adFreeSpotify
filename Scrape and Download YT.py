from pytube import YouTube
import urllib.request
import re

lis = ['Fighter - The Score', 'Renegade - Zayde Wølf', 'Legend - The Score']

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
    print(URL)
    downloadFolder = "C:/Users/LAKSHYA KUMAR/PycharmProjects/pythonProject/songDownloads"
    name = str(songName) + ".mp3"
    yt = YouTube(URL)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=downloadFolder, filename=name)


for item in lis:
    search = scrapeYt(item)
    downloadVideo(search, item)
    print("Downloaded  " + item)


