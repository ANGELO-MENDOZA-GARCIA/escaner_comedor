import tkinter as tk
from pynput import keyboard

class BarcodeScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner de Código de Barras")
        self.root.geometry("400x200")
        
        # Variables para la interfaz
        self.status_var = tk.StringVar(value="Escáner conectado. Listo para escanear.")
        self.code_var = tk.StringVar(value="")

        # Etiquetas en la interfaz
        tk.Label(root, textvariable=self.status_var, font=("Arial", 14)).pack(pady=20)
        tk.Label(root, textvariable=self.code_var, font=("Arial", 16), fg="green").pack(pady=20)

        # Escucha en segundo plano
        self.current_code = ""
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, key):
        try:
            # Capturar caracteres y construir el código
            if key.char is not None:
                self.current_code += key.char
        except AttributeError:
            # Enter finaliza la captura del código
            if key == keyboard.Key.enter:
                self.code_var.set(f"Código escaneado: {self.current_code}")
                self.current_code = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeScannerApp(root)
    root.mainloop()
