import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

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

def insertar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO misdatos (id, nombres, apellidos, telefono, email) VALUES (%s, %s, %s, %s, %s)"
    valores = (entry_id.get(), entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_email.get())
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Información", "Registro insertado con éxito")
        limpiar_campos()
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def editar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE misdatos SET nombres=%s, apellidos=%s, telefono=%s, email=%s WHERE id=%s"
    valores = (entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_email.get(), entry_id.get())
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Información", "Registro actualizado con éxito")
        limpiar_campos()
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def buscar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM misdatos WHERE id=%s"
    valores = (entry_id.get(),)
    try:
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()
        if resultado:
            entry_nombre.delete(0, tk.END)
            entry_apellido.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            entry_email.delete(0, tk.END)

            entry_nombre.insert(0, resultado[1])
            entry_apellido.insert(0, resultado[2])
            entry_telefono.insert(0, resultado[3])
            entry_email.insert(0, resultado[4])
        else:
            messagebox.showinfo("Información", "No se encontró el registro")
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def eliminar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM misdatos WHERE id=%s"
    valores = (entry_id.get(),)
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Información", "Registro eliminado con éxito")
        limpiar_campos()
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Crear la ventana principal
app = tk.Tk()
app.title("Formulario de datos personales")

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

# Botones
ttk.Button(app, text='Insertar', command=insertar).grid(column=0, row=5, padx=5, pady=5)
ttk.Button(app, text='Editar', command=editar).grid(column=1, row=5, padx=5, pady=5)
ttk.Button(app, text='Buscar', command=buscar).grid(column=0, row=6, padx=5, pady=5)
ttk.Button(app, text='Eliminar', command=eliminar).grid(column=1, row=6, padx=5, pady=5)
ttk.Button(app, text='Limpiar', command=limpiar_campos).grid(column=0, row=7, columnspan=2, pady=10)

# Iniciar el bucle principal de la aplicación
app.mainloop()
