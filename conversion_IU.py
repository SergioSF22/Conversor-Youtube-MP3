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

def start_download():
    youtube_url = url_entry.get()
    output_directory = dir_entry.get()
    if not youtube_url or not output_directory:
        messagebox.showerror("Error", "Debe ingresar una URL y seleccionar un directorio")
        return
    
    try:
        download_youtube_audio(youtube_url, output_directory)
        messagebox.showinfo("Éxito", "Descarga y conversión completadas.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_directory():
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
