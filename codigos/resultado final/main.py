import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from pynput import keyboard

# Conectar a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
            user='root', password='mysql',
            host='localhost',
            database='misdatos',
            port='3306'
        )
        return conexion
    except Error as e:
        messagebox.showerror('Error', str(e))

# Función para manejar el escaneo
def on_key_press(key):
    global current_code
    try:
        if key.char is not None:
            current_code += key.char  # Construir el código escaneado
    except AttributeError:
        if key == keyboard.Key.enter:  # Detectar Enter como fin de escaneo
            buscar(current_code)  # Buscar el colaborador con el código escaneado
            current_code = ""  # Reiniciar el código actual

# Buscar el colaborador en la base de datos
def buscar(numero_colaborador):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM misdatos WHERE numero_colaborador=%s"
    try:
        cursor.execute(sql, (numero_colaborador,))
        registro = cursor.fetchone()
        if registro:
            entry_nombre.delete(0, tk.END)
            entry_apellido.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            # Insertar los datos encontrados en los campos de texto
            entry_nombre.insert(0, registro[1])
            entry_apellido.insert(0, registro[2])
            entry_telefono.insert(0, registro[3])
            entry_email.insert(0, registro[4])
        else:
            messagebox.showinfo('Información', 'No se encontró el registro solicitado')
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

# Limpiar los campos
def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Variables y configuración inicial
current_code = ""

# Crear la ventana principal
app = tk.Tk()
app.title("Escáner de Colaboradores")

# Etiqueta y entrada para el ID
ttk.Label(app, text="ID: ").grid(column=0, row=0, padx=5, pady=5)
entry_id = ttk.Entry(app)
entry_id.grid(column=1, row=0, padx=5, pady=5)

# Etiqueta y entrada para el Nombre
ttk.Label(app, text="Nombre: ").grid(column=0, row=1, padx=5, pady=5)
entry_nombre = ttk.Entry(app)
entry_nombre.grid(column=1, row=1, padx=5, pady=5)

# Etiqueta y entrada para el Apellido
ttk.Label(app, text="Apellido: ").grid(column=0, row=2, padx=5, pady=5)
entry_apellido = ttk.Entry(app)
entry_apellido.grid(column=1, row=2, padx=5, pady=5)

# Etiqueta y entrada para el Teléfono
ttk.Label(app, text="Teléfono: ").grid(column=0, row=3, padx=5, pady=5)
entry_telefono = ttk.Entry(app)
entry_telefono.grid(column=1, row=3, padx=5, pady=5)

# Etiqueta y entrada para el Email
ttk.Label(app, text="Email: ").grid(column=0, row=4, padx=5, pady=5)
entry_email = ttk.Entry(app)
entry_email.grid(column=1, row=4, padx=5, pady=5)

# Botón para limpiar los campos
ttk.Button(app, text='Limpiar', command=limpiar_campos).grid(column=0, row=5, padx=5, pady=5)

# Iniciar la escucha de teclado en segundo plano para escanear el código
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

# Ejecutar la aplicación
app.mainloop()
