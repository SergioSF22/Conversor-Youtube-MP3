import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_youtube_audio(youtube_url, output_directory):
    """
    Descarga y convierte un video o una playlist de YouTube a WAV.
    :param youtube_url: URL del video o playlist de YouTube.
    :param output_directory: Directorio donde se guardarán los archivos WAV.
    """
    # Crea el directorio de salida si no existe
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Configuración de la descarga
    ydl_opts = {
        'format': 'bestaudio/best', # Selecciona la mejor calidad de audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }], # Selecciona el formato de audio deseado
        'outtmpl': os.path.join(output_directory, '%(playlist_title)s/%(title)s.%(ext)s'), # Define el nombre del archivo de salida
        'quiet': False, # Desactiva el modo quiet para mostrar mensajes de ejecución mas detallados
        'noplaylist': False  # Permite descargar playlists completas
    }
    
    # Ejecuta la descarga y la conversión con un manejo de errores
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Error de Descarga", f"Error al descargar: {str(e)}")
    except yt_dlp.utils.ExtractorError as e:
        messagebox.showerror("Error de Extracción", f"Error al extraer información: {str(e)}")
    except yt_dlp.utils.PostProcessingError as e:
        messagebox.showerror("Error de Post-Procesado", f"Error en la conversión del archivo: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error Desconocido", f"Ocurrió un error inesperado: {str(e)}")

def start_download():
    """
    Inicia la descarga y la conversión de un video o una playlist de YouTube.
    """
    youtube_url = url_entry.get()
    output_directory = dir_entry.get()
    if not youtube_url or not output_directory:
        messagebox.showerror("Error", "Debe ingresar una URL y seleccionar un directorio")
        return
    
    download_youtube_audio(youtube_url, output_directory)
    messagebox.showinfo("Éxito", "Descarga y conversión completadas.")
   

def browse_directory():
    """
    Permite al usuario elegir el directorio destino al pulsar el botón 'Seleccionar'.
    """
    directory = filedialog.askdirectory()
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, directory)

# Crear ventana principal
root = tk.Tk()
root.title("YouTube a MP3")
root.geometry("600x300")

tk.Label(root, text="URL de YouTube:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Directorio de Descarga:").pack(pady=5)
dir_entry = tk.Entry(root, width=50)
dir_entry.pack(padx=5, pady=10)

browse_button = tk.Button(root, text="Seleccionar", command=browse_directory)
browse_button.pack(padx=5)

download_button = tk.Button(root, text="Descargar", command=start_download)
download_button.pack(pady=20)

root.mainloop()
