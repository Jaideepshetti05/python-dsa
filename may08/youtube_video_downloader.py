from pytube import YouTube

url = input("Enter YouTube URL: ")

yt = YouTube(url)
video = yt.streams.first()

video.download()

print("Download Completed!")