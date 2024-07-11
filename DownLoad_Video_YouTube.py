from pytube import YouTube

def baixar_video(url):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)

        # Seleciona a stream de maior resolução disponível
        stream = yt.streams.get_highest_resolution()

        # Baixa o vídeo para o caminho especificado
        stream.download(output_path=caminho_destino)
        print(f"Download concluído! Vídeo salvo em: {caminho_destino}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

# Exemplo de uso
url_video = input("Digite a URL do vídeo que deseja!: ")
baixar_video(url_video)