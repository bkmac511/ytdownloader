from pytube import YouTube

link = input("Podaj link do nagrania z YouTube: ")

yt = YouTube(link)

video = yt.streams.first()

video.download('C:/Users/Bartek/Videos')
