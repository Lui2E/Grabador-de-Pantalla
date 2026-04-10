# 🎥 Grabadora de Pantalla en PYTHON (Windows)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

Una herramienta profesional y ligera desarrollada en **Python** para la captura de pantalla completa en entornos Windows. Permite grabar movimientos del mouse, apertura de ventanas y aplicaciones con alta fidelidad, ofreciendo una interfaz gráfica intuitiva y soporte para atajos de teclado globales.

---

## 📺 Demo en Acción

¡Mira cómo funciona la aplicación en este video demostrativo!

[![Mira el video aquí](https://i.ytimg.com/vi/UuoFenSOZO0/maxresdefault.jpg)](https://www.youtube.com/watch?v=UuoFenSOZO0)

*Haz clic en la imagen para ver el video en YouTube.*

---

## 📋 Tabla de Contenidos
1. [Características Principales](#-características-principales)
2. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
3. [Instalación y Requisitos](#-instalación-y-requisitos)
4. [Uso y Atajos](#-uso-y-atajos)
5. [Compilación a Ejecutivo (.EXE)](#-compilación-a-ejecutivo-exe)
6. [Notas Técnicas](#-notas-técnicas)

---

## ✨ Características Principales

* **Captura Total:** Graba toda la pantalla, incluyendo el cursor del mouse y ventanas emergentes.
* **Interfaz Gráfica (GUI):** Panel de control sencillo con selector de resolución.
* **Atajos Globales:** Inicia y detiene la grabación con la tecla **F9**, incluso si la app está minimizada.
* **Resoluciones Configurables:** Soporte para Full HD, 720p y 480p para optimizar el peso del archivo.
* **Gestión de Archivos:** Guardado automático en formato **MP4** con explorador de archivos para elegir destino.
* **Compatibilidad UAC:** Capacidad para seguir grabando incluso ante ventanas con permisos de administrador (requiere ejecución como admin).

---

## ⚙️ Tecnologías Utilizadas

* **[OpenCV (cv2)](https://opencv.org/):** Procesamiento y codificación del flujo de video.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Captura de frames de pantalla de alta precisión.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Desarrollo de la interfaz de usuario.
* **[Pynput](https://pynput.readthedocs.io/):** Control y monitoreo de eventos de teclado global.
* **[Threading](https://docs.python.org/3/library/threading.html):** Manejo de procesos en segundo plano para evitar congelamiento de la GUI.
* **[NumPy](https://numpy.org/):** Manipulación eficiente de matrices de imagen.

---

## 🛠️ Instalación y Requisitos

### Prerrequisitos
* Windows 10 o superior.
* Python 3.10+ instalado.

### Pasos
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TuUsuario/Grabador-de-Pantalla.git](https://github.com/TuUsuario/Grabador-de-Pantalla.git)
   cd Grabador-de-Pantalla
   ```

2. **Instalar dependencias necesarias:**
   ```bash
   pip install opencv-python pyautogui numpy pynput
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

### Uso y Atajos
1. **Selección:** Elige la resolución deseada en el menú desplegable.

2. **Grabación:** Haz clic en el botón verde o presiona F9 para comenzar.

3. **Finalización:** Haz clic en el botón rojo (Detener) o presiona F9 nuevamente.

4. **Guardado:** Al finalizar, se abrirá una ventana de Windows. Selecciona la carpeta de destino y el nombre de tu video (.mp4).

  >[!IMPORTANT]
  >Para grabar ventanas de sistema o instaladores que requieren permisos, ejecuta el programa o VS Code como Administrador.

## 📦 Compilación a Ejecutivo (.EXE)

Si deseas generar una aplicación independiente que no requiera tener Python instalado, utiliza **PyInstaller**:

1. Instalar PyInstaller:
   ```bash
   pip install pyinstaller

2. Generar el archivo único:
   ```bash
   pyinstaller --onefile --windowed --name "GrabadoraPro" app.py

El ejecutable se generará en la carpeta /dist.

## 📁 Estructura del Proyecto

      ├── src/
      │   └── app.py            # Código fuente principal
      ├── temp_grabacion.mp4    # Archivo temporal (se autolimpia)
      ├── requirements.txt      # Dependencias del proyecto
      └── README.md             # Documentación

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, ver el archivo LICENSE.

Desarrollado por Luis Enrrique - IT Specialist


   
