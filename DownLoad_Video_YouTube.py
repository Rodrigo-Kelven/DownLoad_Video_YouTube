import yt_dlp

# Faz um input da URL do vídeo que será baixado
url = input("Enter the YouTube video URL: ")

ydl_opts= {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")