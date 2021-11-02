from pytube import YouTube
from colorama import init, Fore, Back, Style
import os
import ffmpeg

init()


def ddl_app ():
    print(Fore.RED + Style.BRIGHT + "Welcome to the Pytube Downloader!" + Style.RESET_ALL)
    url = input(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Input your URL: " + Style.RESET_ALL)

    yt = YouTube(url)

    print(Fore.YELLOW + Style.BRIGHT + "Grabbing Video Itags..." + Style.RESET_ALL)

    for i in list(yt.streams):
        print(i)

    itag = input(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Input Itag of Video: " + Style.RESET_ALL)

    print(Fore.MAGENTA + Style.BRIGHT + "Downloading Video..." + Style.RESET_ALL)
    video = yt.streams.get_by_itag(int(itag)).download()
    os.rename(video,"video_1080.mp4")

    print(Fore.GREEN + Style.BRIGHT + "****** Video download completed! ******" + Style.RESET_ALL)

    print(Fore.YELLOW + Style.BRIGHT + "Grabbing Audio Itags..." + Style.RESET_ALL)

    for i in list(yt.streams):
        print(i)

    itag = input(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Input Itag of Audio: " + Style.RESET_ALL)

    print(Fore.MAGENTA + Style.BRIGHT + "Downloading Audio..." + Style.RESET_ALL)
    audio = yt.streams.get_by_itag(int(itag)).download()
    os.rename(audio,"audio.mp4")

    print(Fore.GREEN + Style.BRIGHT + "****** Audio download completed! ******" + Style.RESET_ALL)

    print(Fore.MAGENTA + Style.BRIGHT + "Merging Video and Audio files..." + Style.RESET_ALL)

    name = input(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Filename of Output File: " + Style.RESET_ALL)

    filename = "%s.mp4" % name

    video_stream = ffmpeg.input('video_1080.mp4')
    audio_stream = ffmpeg.input('audio.mp4')
    ffmpeg.output(audio_stream, video_stream, filename).run()

    print(Fore.GREEN + Style.BRIGHT + "****** Merging Video and Audio files completed! ******" + Style.RESET_ALL)

    print(Fore.MAGENTA + Style.BRIGHT + "Removing files..." + Style.RESET_ALL)

    os.remove("video_1080.mp4")
    os.remove("audio.mp4")

    print(Fore.GREEN + Style.BRIGHT + "****** Files remove! ******" + Style.RESET_ALL)

    print(Fore.GREEN + Style.BRIGHT + "****** Job done! Have fun with your video! ******" + Style.RESET_ALL)

ddl_app()
