# Conversor Youtube MP3

Si estas cansado de utilizar los conversores youtube-mp3 de internet, de esos tiempo de espera tan largos y de esas limitaciones tan absurdas que poseen algunos has llegado al sitio indicado. Estaba cansado de tener que elegir entre los miles de conversores de terceros que hay en internet asi que, decidí crear el mío propio.

## ¿Por qué usarlo?

Este conversor proporciona una solución de descarga y conversión de videos de YouTube que no depende de descargadores de terceros. Es una herramienta simple pero poderosa que te permite controlar las descargas y conversiones de tus videos. Además, esta totalmente programado en Python lo cual permite una integración mucha mas sencilla con el usuario inexperto.

## Funcionalidades

- **Conversión de videos y playlist:** Puedes convertir practicamente cualquier video de Youtube a formato MP3, WAV o MP4 proporcionando la URL. También puedes convertir Playslist enteras de la misma manera.

- **Calidad máxima:** La configuración de la conversión está diseñada de manera que obtengas la mejor calidad del formato seleccionado al realizarla.

- **Modos:** Contiene dos modos diferentes de uso:
    - **Por consola:** Ejecutando el fichero de nombre *conversion.py* se realizara la ingresión de datos por consola.
    - **Por interfaz gráfica (solo MP3):** Ejecutando el fichero de nombre *conversion_IU.py* se realizara la ingresión de los datos por una interfaz gráfica simple implementada por la librería TKinter.

## Dependencias

Para usar el conversor primero hay que instalar ciertas herramientas:

1. Primero de todo y mas importante, **Python**: 
- Nos dirigimos a la página oficial de [Python](https://www.python.org/downloads/) para descargarlo. (Yo he usado la versión **3.13.1**)
- **IMPORTANTE**: Al proceder con la instalación marcar la opción de 'Agregar variables de entorno al PATH' para evitar tener que agregarlas a mano posteriormente.
- Una vez instalado verificar la instalación en consola con  ```` python --version ````  o ``` py --version ```

2. Instalar **ffmpeg** (librería encargada de la conversión de los archivos):
- Nos dirigimos a la página oficial de descargas de [ffmpeg](https://www.ffmpeg.org/download.html)
- Una vez instalado debemos agregar a las variables del sistema (PATH) la carpeta /bin ubicada dentro de la carpeta descargada.
- Ejecutamos el comnando ``` ffmpeg -version ``` en la consola para verificar la instalación.

3. Una vez hecho esto debemos instalar las librerias que importará y usará python en el código de nuestro programa. Para este paso RECOMIENDO (es decir, no es obligatorio) instalar un entorno virtual en la carpeta de nuestro proyecto para no instalar las librerias en nuestro entorno global. ([Crear entornos virtuales mediante venv](https://docs.python.org/es/3.13/tutorial/venv.html))
- Abrimos una terminal dentro de la carpeta de este proyecto activando nuestro entorno virtual (si lo creaste) y ejecutamos el comando ``` pip install -r requirements.txt ``` (**IMPORTANTE**: Si obtienes un error indicando que 'pip' no se reconoce como comando del sistema significa que no tenemos las variables de entorno definidas en el PATH y debes configurarlas a mano. [Tutorial](https://www.youtube.com/watch?v=4EGfl6sWQ18))

## Como usar

- Si optas por la opcion de **consola**:
    - Dirigete a la carpeta del proyecto y abre una terminal.
    - Ejecuta el comando ```python .\conversion.py``` o  ```py .\conversion.py```
    - Introduce la ruta absoluta o relativa de la carpeta donde quieres guardar los archivos convertidos (Si la carpeta no existe, la creará).
    - Selecciona el formato de conversión deseado (MP3, WAV, MP4)
    - Introduce la URL del vídeo o playlist que deseas convertir.
    - Una vez acabada la conversión decide si quieres continuar o acabar el programa.
- Si optas por la opción de **interfaz gráfica**:
    - Introduce la URL del video o playlist a descargar en el cuadro de texto debajo de la etiqueta *URL de Youtube*
    - Selecciona la carpeta destino donde guardar los archivos mediante el boton *'Seleccionar'* o introduciendo la ruta relativa o absoluta en el cuadro de texto debajo de la etiqueta *'Directorio de descarga'* (Si la carpeta no existe, la creará).
    - Pulsa el botón *'Descargar'*.

¡Disfruta de tu videos en el formato deseado!

## Factores a tener en cuenta

- Yo he utilizado la versión de **Python 3.13.1** por lo que desconozco si la herramienta funciona en otras versiones (recomiendo instalar la misma).
- Es posible que ciertos vídeos no puedan ser convertidos debido a restricciones regionales o privacidad de los mismos.
- Si al realizar cualquier conversión esta va muy lenta y aparece un **WARNING** que dice lo siguiente: ```Signature extraction failed: Some formats may be missing```. Siginifica que YouTube ha cambiado su sistema de encriptación de firmas, lo que requiere una actualización de la biblioteca de ```yt_dlp```. (Comando: ```pip install -U yt-dlp```)