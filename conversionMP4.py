import os
import yt_dlp

def download_youtube_audio(youtube_url, output_directory):
    """
    Descarga y convierte un video o una playlist de YouTube a MP3.
    :param youtube_url: URL del video o playlist de YouTube.
    :param output_directory: Directorio donde se guardarán los archivos MP3.
    """
    # Crea el directorio de salida si no existe
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Configuración de la descarga
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', # Selecciona la mejor calidad de audio
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_directory, '%(playlist_title)s/%(title)s.%(ext)s'), # Define el nombre del archivo de salida
        'quiet': False, # Desactiva el modo quiet para mostrar mensajes de ejecución mas detallados
        'noplaylist': False # Permite descargar playlists completas
    }
    # Ejecuta la descarga y la conversión con un manejo de errores
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Error de descarga: {e}")
    except yt_dlp.utils.ExtractorError as e:
        print(f"Error al extraer información: {e}")
    except yt_dlp.utils.PostProcessingError as e:
        print(f"Error en el postprocesado: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Programa principal
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
