import os
import yt_dlp

# Faz um input da URL do vídeo que será baixado
url = input("Enter the YouTube video URL: ")

# Nome da pasta onde as músicas serão salvas
nome_pasta = "musicas"

# Criando a pasta se ela não existir
if not os.path.exists(nome_pasta):
    os.mkdir(nome_pasta)

# Opções do yt-dlp para especificar o diretório de saída
ydl_opts = {
    'outtmpl': os.path.join(nome_pasta, '%(title)s.%(ext)s')  # Define o caminho de saída com o nome do arquivo
}

# Salva todos os vídeos baixados na pasta especificada
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")