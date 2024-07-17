import yt_dlp

def baixar_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Define o formato de saída do arquivo
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        },
        # 'cookiefile': 'cookies.txt',  # Descomente e forneça o caminho para o arquivo de cookies se necessário
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completo!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Erro ao baixar o vídeo: {e}")

# Exemplo de uso
url_video = input("Coloque a URL que deseja: ")
baixar_video(url_video)