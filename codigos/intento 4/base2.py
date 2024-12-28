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
    sql = "UPDATE misdatos SET id=%s, nombres=%s, apellidos=%s, telefono=%s WHERE email=%s"
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

def eliminar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM misdatos WHERE id=%s"
    try:
        cursor.execute(sql, (entry_id.get(),))
        conexion.commit()
        messagebox.showinfo("Información", "Registro eliminado con éxito")
        limpiar_campos()
    except Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def buscar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM misdatos WHERE id=%s"
    try:
        cursor.execute(sql, (entry_id.get(),))
        registro = cursor.fetchone()
        if registro:
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

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
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

ttk.Button(app,text='Insertar', command=insertar).grid(column=0, row=5)
ttk.Button(app,text='Editar', command=editar).grid(column=1, row=5)
ttk.Button(app,text='Buscar', command=buscar).grid(column=2, row=5)
ttk.Button(app,text='Eliminar', command=eliminar).grid(column=3, row=5)
ttk.Button(app,text='Limpiar', command=limpiar_campos).grid(column=4, row=5)



app.mainloop()