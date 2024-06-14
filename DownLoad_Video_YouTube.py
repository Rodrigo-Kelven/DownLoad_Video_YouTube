import yt_dlp 

#faz um input da URL do vídeo que será baixado
url = input("Enter the YouTube video URL: ")

ydl_opts = {}

#salva todos os vídeos baixados
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")