import os
import yt_dlp
import re

# Expresión regular para validar una URL de YouTube
YOUTUBE_URL_REGEX = re.compile(
    r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
)

# Diccionario de parámetros de conversión sin la ruta de salida
conversion_parameters = {
    'MP3': {
        'format': 'bestaudio/best', # Selecciona la mejor calidad de audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }], # Selecciona el formato de audio deseado
        'quiet': False, # Desactiva el modo quiet para mostrar mensajes de ejecución mas detallados
        'noplaylist': False, # Permite descargar playlists completas
        'ignoreerrors': True # Ignora errores de descarga
    },
    'WAV': {
        'format': 'bestaudio/best', # Selecciona la mejor calidad de audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }], # Selecciona el formato de audio deseado
        'quiet': False, # Desactiva el modo quiet para mostrar mensajes de ejecución mas detallados
        'noplaylist': False, # Permite descargar playlists completas
        'ignoreerrors': True # Ignora errores de descarga
    },
    'MP4': {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', # Selecciona la mejor calidad de audio y video
        'merge_output_format': 'mp4', # Define el formato de salida para la mezcla
        'quiet': False, # Desactiva el modo quiet para mostrar mensajes de ejecución mas detallados
        'noplaylist': False, # Permite descargar playlists completas
        'ignoreerrors': True # Ignora errores de descarga
    }
}

def get_conversion_type():
    """ Solicita al usuario el tipo de conversión y lo valida. """
    while True:
        conversion_type = input("Ingrese el tipo de conversión (MP3, WAV, MP4): ").upper()
        if conversion_type in conversion_parameters:
            return conversion_type
        print("Entrada no válida. Por favor, ingrese 'MP3', 'WAV' o 'MP4'.")

def get_valid_directory():
    """ Solicita y valida que el directorio de descarga sea válido. """
    while True:
        output_directory = input("Ingrese el directorio de descarga: ").strip()
        if not output_directory:
            print("Error: No puede dejar el campo vacío. Intente nuevamente.")
            continue
        if not os.path.exists(output_directory):
            try:
                os.makedirs(output_directory)  # Crea el directorio si no existe
                print(f"Directorio '{output_directory}' creado correctamente.")
            except OSError as e:
                print(f"Error al crear el directorio: {e}")
                continue
        return output_directory

def get_valid_youtube_url():
    """ Solicita y valida que la URL sea una URL válida de YouTube. """
    while True:
        youtube_url = input("Ingrese la URL del video o playlist de YouTube: ").strip()
        if not youtube_url:
            print("Error: La URL no puede estar vacía. Intente nuevamente.")
            continue
        if not YOUTUBE_URL_REGEX.match(youtube_url):
            print("Error: La URL ingresada no parece ser una URL válida de YouTube. Intente nuevamente.")
            continue
        return youtube_url

def download_youtube_audio(youtube_url, output_directory, conversion_type):
    """
    Descarga y convierte un video o una playlist de YouTube según el formato seleccionado.
    """
    # Configuración de los parámetros de conversión
    selected_conversion_opts = conversion_parameters[conversion_type].copy()
    selected_conversion_opts['outtmpl'] = os.path.join(output_directory, '%(playlist_title)s/%(title)s.%(ext)s')

    try:
        with yt_dlp.YoutubeDL(selected_conversion_opts) as ydl:
            ydl.download([youtube_url])
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Error de descarga: {e}\nVerifique la URL e intente nuevamente.")
    except yt_dlp.utils.ExtractorError as e:
        print(f"❌ Error al extraer información: {e}")
    except yt_dlp.utils.PostProcessingError as e:
        print(f"❌ Error en el postprocesado: {e}")
    except FileNotFoundError as e:
        print(f"❌ Error: No se encontró la ruta especificada: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    output_directory = get_valid_directory()
    conversion_type = get_conversion_type()

    while True:
        youtube_url = get_valid_youtube_url()  # Ahora validamos que sea una URL correcta
        download_youtube_audio(youtube_url, output_directory, conversion_type)
        print("✅ Descarga y conversión completadas.")

        continuar = input("¿Desea descargar otro video o playlist? (S/N): ").strip().upper()
        if continuar == 'N':
            break