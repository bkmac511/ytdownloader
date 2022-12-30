from pytube import YouTube

link = input("Podaj link do nagrania z YouTube: ")

yt = YouTube(link)

all_streams = yt.streams

resolutions = set()

for stream in all_streams:
    resolutions.add(stream.resolution)

print("Dostępne rozdzielczości:")
for i, resolution in enumerate(resolutions):
    print(f"{i+1}. {resolution}")

resolution = input("Wybierz rozdzielczość (np. 1920x1080): ")

filtered_streams = all_streams.filter(res=resolution)

if filtered_streams:
    chosen_stream = filtered_streams[0]
    chosen_stream.download('C:/Users/Bartek/Videos')
else:
    print(f"Nie znaleziono nagrania w rozdzielczości {resolution}. Spróbuj wybrać inną.")
