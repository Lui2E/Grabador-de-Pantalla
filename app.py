import cv2
import pyautogui
import numpy as np
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from pynput import keyboard
import shutil
import os

class GrabadoraPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Screen Recorder")
        self.root.geometry("300x250")
        
        self.grabando = False
        self.resolucion = tk.StringVar(value="Full HD")
        
        # --- Interfaz Gráfica ---
        tk.Label(root, text="Grabadora de Pantalla", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Seleccionar Resolución:").pack()
        opciones_res = ["Full HD", "720p", "480p"]
        tk.OptionMenu(root, self.resolucion, *opciones_res).pack(pady=5)

        self.btn_accion = tk.Button(root, text="Iniciar Grabación (F9)", 
                                   command=self.toggle_grabacion, bg="green", fg="white")
        self.btn_accion.pack(pady=20, ipadx=10)
        
        tk.Label(root, text="Presiona F9 para Iniciar/Detener", fg="gray").pack()

        # --- Listener de Teclado Global (F9) ---
        self.listener = keyboard.Listener(on_press=self.al_presionar_tecla)
        self.listener.start()

    def al_presionar_tecla(self, key):
        if key == keyboard.Key.f9:
            self.root.after(0, self.toggle_grabacion)

    def obtener_dimensiones(self):
        res_map = {
            "Full HD": tuple(pyautogui.size()),
            "720p": (1280, 720),
            "480p": (854, 480)
        }
        return res_map[self.resolucion.get()]

    def toggle_grabacion(self):
        if not self.grabando:
            self.iniciar_grabacion()
        else:
            self.detener_grabacion()

    def iniciar_grabacion(self):
        self.grabando = True
        self.btn_accion.config(text="DETENER (F9)", bg="red")
        self.hilo = threading.Thread(target=self.proceso_grabacion)
        self.hilo.start()

    def detener_grabacion(self):
        self.grabando = False
        self.btn_accion.config(text="Iniciar Grabación (F9)", bg="green")

    def proceso_grabacion(self):
        dim = self.obtener_dimensiones()
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        temp_filename = "temp_grabacion.mp4"
        out = cv2.VideoWriter(temp_filename, fourcc, 20.0, dim)

        while self.grabando:
            try:
                # Captura de pantalla con manejo de excepciones para evitar cierres por UAC
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                if dim != tuple(pyautogui.size()):
                    frame = cv2.resize(frame, dim)
                    
                out.write(frame)
            except Exception as e:
                # Si falla la captura (por una ventana de Admin), imprime el aviso y sigue intentando
                print(f"Aviso: Captura omitida temporalmente (Posible falta de permisos): {e}")
                continue
        
        out.release()
        self.root.after(0, lambda: self.guardar_archivo(temp_filename))

    def guardar_archivo(self, temp_file):
        path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("Video MP4", "*.mp4")],
            title="Guardar grabación como..."
        )
        
        if path:
            try:
                shutil.move(temp_file, path)
                messagebox.showinfo("Éxito", f"Video guardado correctamente en:\n{path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el video: {e}")
        else:
            if os.path.exists(temp_file):
                os.remove(temp_file)
            messagebox.showwarning("Aviso", "La grabación fue descartada.")

if __name__ == "__main__":
    app_root = tk.Tk()
    app = GrabadoraPro(app_root)
    app_root.mainloop()