import os
import yt_dlp

def download_youtube_audio(youtube_url, output_directory):
    """
    Descarga y convierte un video o una playlist de YouTube a MP3.
    :param youtube_url: URL del video o playlist de YouTube.
    :param output_directory: Directorio donde se guardarán los archivos MP3.
    """
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_directory, '%(playlist_title)s/%(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': False  # Permite descargar playlists completas
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    output_directory = input("Ingrese el directorio de descarga: ")
    while True:
        youtube_url = input("Ingrese la URL del video o playlist de YouTube: ")
        download_youtube_audio(youtube_url, output_directory)
        print("Descarga y conversión completadas.")
        
        while True:
            continuar = input("¿Desea descargar otro video o playlist? (S/N): ").strip().upper()
            if continuar in ['S', 'N']:
                break
            print("Entrada no válida. Por favor, ingrese 'S' para continuar o 'N' para salir.")
        
        if continuar == 'N':
            break
