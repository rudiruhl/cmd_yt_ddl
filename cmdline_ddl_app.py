from pytube import YouTube
import os
import ffmpeg

def ddl_app ():
    print("Welcome to the Pytube Downloader!")
    url = input("URL: ")

    yt = YouTube(url)

    print("Download Video")

    for i in list(yt.streams):
        print(i)

    itag = input("Itag of Video: ")
    video = yt.streams.get_by_itag(int(itag)).download()
    os.rename(video,"video_1080.mp4")

    print("Download Audio")

    for i in list(yt.streams):
        print(i)

    itag = input("Itag of Audio: ")
    audio = yt.streams.get_by_itag(int(itag)).download()
    os.rename(audio,"audio.mp4")

    print("Merging Video + Audio")

    name = input("Name of Video File: ")
    filename = "%s.mp4" % name

    video_stream = ffmpeg.input('video_1080.mp4')
    audio_stream = ffmpeg.input('audio.mp4')
    ffmpeg.output(audio_stream, video_stream, filename).run()

    os.remove("video_1080.mp4")
    os.remove("audio.mp4")
    print("Files Removed!")

ddl_app()
